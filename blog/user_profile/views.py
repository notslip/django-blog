from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from .models import UserProfile
from .forms import UserForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(DetailView):
    def get(self, request, **kwargs):
        if 'pk' in kwargs:
            userprofile = UserProfile.objects.get(id=kwargs['pk'])
        else:
            userprofile = request.user.userprofile
        return render(request, template_name='user_profile/profile.html', context={'userprofile': userprofile})


class ProfileUpdate(LoginRequiredMixin, UpdateView):

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_detail_url')
        else:
            return render(request, template_name='user_profile/profile_update.html', context={
                                                                                            'user_form': user_form,
                                                                                            'profile_form': profile_form
                                                                                        })

    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        return render(request, template_name='user_profile/profile_update.html', context={
                                                                                        'user_form': user_form,
                                                                                        'profile_form': profile_form
                                                                                        })




