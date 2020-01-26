from django.contrib.auth.models import User
from blogengine.models import Post, Tag
from comments.models import Comment

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import CreateUserForm
from django.db.models import Q


class CreateUser(CreateView):

    model = User
    form_class = CreateUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


def search_list(request):

    search_query = request.GET.get('search','')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        tags = Tag.objects.filter(title__icontains=search_query)
        comments = Comment.objects.filter(text__icontains=search_query)

        return render(request, 'search/search.html', context={'posts':posts, 'tags':tags, 'comments': comments, 'search_query':search_query})




