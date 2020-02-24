from django.contrib.auth.models import User
from blogengine.models import Post, Tag
from comments.models import Comment
from django.core.mail import EmailMessage
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .forms import CreateUserForm
from django.db.models import Q
from hashlib import sha1


def send_activate_email(user, **kwargs):
    hash = sha1(bytes('{}'.format(user.username), encoding='utf-8')).hexdigest()
    link = '/'.join(['http://127.0.0.1:8000/activated', hash])
    msg = EmailMessage(
        subject='Активация на сайте',
        body='Перейдите по ссылке что бы активировать профиль: {}'.format(link),
        from_email='admin@gmail.com',
        to=(user.email,),
        headers={'From': 'email_from@me.com'}
    )
    msg.send()


class CreateUser(CreateView):

    model = User
    form_class = CreateUserForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


    @receiver(pre_save, sender=User)
    def set_new_user_inactive(sender, instance, **kwargs):
        if instance._state.adding is True:
            print("Creating Inactive User")
            send_activate_email(instance)
            instance.is_active = False
        else:
            print("Updating User Record")



def activated_user(request, hash):
    # try:
        id_list=User.objects.filter(is_active=False)
        for user in id_list:
            if sha1(bytes('{}'.format(user.username), encoding='utf-8')).hexdigest() == hash:
                user.is_active=True

                user.save(force_update=True)
                msg = EmailMessage(
                    subject='Активация на сайте',
                    body='Активация профиля {} прошла успешно'.format(user.username),
                    from_email='notslip1991@gmail.com',
                    to=(user.email,),
                    headers={'From': 'email_from@me.com'}
                )
                msg.send()
    # except Exception:
    #     print('Erorr')
        return redirect('login')





def search_list(request):

    search_query = request.GET.get('search','')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        tags = Tag.objects.filter(title__icontains=search_query)
        comments = Comment.objects.filter(text__icontains=search_query)

        return render(request, 'search/search.html', context={'posts':posts, 'tags':tags, 'comments': comments, 'search_query':search_query})




