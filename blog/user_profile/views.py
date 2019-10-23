from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from .models import UserProfile
from .forms import UserForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from blog import settings


class ProfileView(DetailView):
    def get(self, request, **kwargs):
        if 'pk' in kwargs:
            userprofile = UserProfile.objects.get(id=kwargs['pk'])
            return render(request, template_name='user_profile/profile.html', context={'userprofile': userprofile})
        elif not request.user.is_authenticated:
            return redirect("{}?next={}".format(settings.LOGIN_URL, request.path))
        else:
            userprofile = request.user.userprofile
            messages_out = userprofile.get_messages_author()
            messages_to = userprofile.get_messages_to()
            return render(request, template_name='user_profile/profile.html', context={'userprofile': userprofile,
                                                                                       'messages_out': messages_out,
                                                                                       'messages_to': messages_to})




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




