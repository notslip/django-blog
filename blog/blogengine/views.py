from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Post, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .forms import TagForm, PostCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#CRUD Post

# def posts_list(request):
#     posts = Post.objects.all()
#     # print(request)
#     return render(request, 'blogengine/index.html', context={'posts': posts})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blogengine/post.html', context={'post': post})

# def post_create(request):
#     if request.method == 'GET':
#         form = PostForm()
#         return render(request, 'blogengine/post_create.html', context={'form': form})
#     else:
#         bound_form = PostForm(request.POST)
#         if bound_form.is_valid():
#             new_post = bound_form.save()
#             return redirect(new_post)

class PostsView(ListView):
    model = Post
    template_name = 'blogengine/index.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogengine/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, slug=self.kwargs['slug'])
        return context


class PostCreate(LoginRequiredMixin, View):

    def get(self, request):
        form = PostCreateForm()
        return render(request, template_name='blogengine/post_create.html', context={'form': form})

    def post(self,request):
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

    # def get_context_data(self, **kwargs):
    #     context = super(PostUpdate, self).get_context_data(**kwargs)
    #     context['post'] = get_object_or_404(Post, slug=self.kwargs['slug'])
    #     return context

    # def get_object_or_404(self):
    #     return Post.objects.get(slug=self.request.GET('slug'))


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name_suffix = '_delete'

    success_url = reverse_lazy('posts_list_url')





#CRUD Tag

# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'blogengine/tags.html', context={'tags': tags})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blogengine/tag.html', context={'tag': tag})

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


class TagUpdate(LoginRequiredMixin, View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        form = TagForm(instance=tag)
        return render(request, 'blogengine/tag_update.html', context={'form': form, 'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        form = TagForm(request.POST, instance=tag)

        if form.is_valid():
            form.save()
            return redirect(tag)
        else:
            return render(request, 'blogengine/tag_update.html', context={'form': form, 'tag': tag})

@login_required()
def tagDelete( request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    if request.method == 'GET':
        return render(request,'blogengine/tag_delete.html', context={'tag': tag})
    else:
        tag.delete()
        return redirect(reverse_lazy('tags_list_url'))



