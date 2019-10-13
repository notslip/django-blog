from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post, Tag
from comments.models import Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .forms import PostCreateForm
from comments.views import CommentAddForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from .settings import PAGINATOR_PER_PAGE


#CRUD Post

class PostsView(ListView):
    model = Post
    template_name = 'blogengine/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        obj = self.model.objects.all()
        paginator = Paginator(obj, PAGINATOR_PER_PAGE)
        page = self.request.GET.get('page')
        if page is None:
            page = 1
        posts = paginator.get_page(page)
        return posts


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogengine/post.html'

    def post(self, request, slug):
        form = CommentAddForm(request.POST)
        post = Post.objects.get(slug__iexact=slug)
        print(post.id)
        print(request.user.userprofile.id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.userprofile
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            raise Exception

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object.id)
        context['form'] = CommentAddForm()
        # print(self.request)
        # print(context)
        return context





class PostCreate(LoginRequiredMixin, View):

    def get(self, request):
        form = PostCreateForm()
        return render(request, template_name='blogengine/post_create.html', context={'form': form})

    def post(self, request):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.userprofile
            post.save()
            return redirect(post)
        else:
            return render(request, 'blogengine/post_create.html', context={'form': form})


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'body', 'tags']
    template_name = 'blogengine/post_update.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = self.model.objects.get(slug=self.kwargs['slug'])
        if obj.is_author( self.request):
            return obj
        else:
            raise PermissionDenied('У вас нет прав на изменение этого поста!')

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url = reverse_lazy('posts_list_url')

    def get_object(self, queryset=None):
        obj = self.model.objects.get(slug=self.kwargs['slug'])
        if obj.is_author(self.request):
            return obj
        else:
            raise PermissionDenied('У вас нет прав на удаление этого поста!')


#CRUD Tag

class TagList(ListView):
    model = Tag
    template_name = 'blogengine/tags.html'
    context_object_name = 'tags'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'blogengine/tag.html'

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return context


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ['title', 'slug']
    template_name = 'blogengine/tag_create.html'


class TagUpdate(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['title', 'slug']
    template_name = 'blogengine/tag_update.html'

    def get_object(self, queryset=None):
        obj = self.model.objects.get(slug=self.kwargs['slug'])
        if self.request.user.is_superuser:
            return obj
        else:
            raise PermissionDenied('У вас нет прав на изменение этого тега!')


@login_required()
def tagDelete(request, slug):
    if request.user.is_superuser:
        tag = Tag.objects.get(slug__iexact=slug)
        if request.method == 'GET':
            return render(request, 'blogengine/tag_delete.html', context={'tag': tag})
        else:
            tag.delete()
            return redirect(reverse_lazy('tags_list_url'))
    else:
        raise PermissionDenied('У вас нет прав на удаление этого тега!')




