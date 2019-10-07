from django.contrib.auth.models import User

from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreateUserForm


class CreateUser(CreateView):

    model = User
    form_class = CreateUserForm
    template_name = 'registration/registration.html'

    success_url = reverse_lazy('login')



