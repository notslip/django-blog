from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from user_profile.models import UserProfile
from .forms import MessageCreateForm1, MessageCreateForm2

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

class MessageCreate(View):


    def get(self, request, **kwargs):
        if 'pk' in kwargs:
            pk=kwargs['pk']
            form = MessageCreateForm1()
            return render(request, template_name='mess/mess_create.html', context={'form': form, 'pk': pk})
        else:
            form = MessageCreateForm2()
            return render(request, template_name='mess/mess_create.html', context={'form': form})

    def post(self, request, **kwargs):
        if 'pk' in kwargs:
            form = MessageCreateForm1(request.POST)
            pk = kwargs['pk']
            to = get_object_or_404(UserProfile, id=pk)
            print(to.__dict__)
            if form.is_valid():
                mess=form.save(commit=False)
                mess.author=request.user.userprofile
                mess.recipient=to
                mess.save()
                return redirect('profile_detail_url')
            else:
                return render(request, template_name='mess/mess_create.html', context={'form': form, 'pk': pk})
        else:
            form = MessageCreateForm2(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.author=request.user.userprofile
                form.save()
                return redirect('profile_detail_url')

