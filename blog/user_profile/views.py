from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.urls import reverse_lazy
from .models import UserProfile


class ProfileView(DetailView):
    model = UserProfile
    template_name = 'user_profile/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileView, self).get_context_data(**kwargs)
    #     context['pk'] = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
    #     print(context)
    #     return context