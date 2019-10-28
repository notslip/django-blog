from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from mess.models import Message



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.TextField(max_length=400, blank=True, db_index=True)
    avatar = models.ImageField(upload_to='avatar/',
                               null=True,
                               blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return 'User profile: {}, user: {}'.format(self.id, self.user.username)

    def get_post(self):
        return UserProfile.objects.get(id=self.id).posts.all()

    def get_comment(self):
        return UserProfile.objects.get(id=self.id).comment.all()

    def get_messages_author(self):
        return UserProfile.objects.get(id=self.id).message_set.all()

    def get_messages_to(self):
        return Message.objects.filter(recipient_id=self.id)


