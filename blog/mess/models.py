from django.db import models
from django.shortcuts import reverse
# from user_profile.models import UserProfile

class Message(models.Model):

    author = models.ForeignKey('user_profile.UserProfile', on_delete=models.CASCADE, blank=True,null=True)
    recipient = models.ForeignKey('user_profile.UserProfile', on_delete=models.CASCADE, blank=True, verbose_name='Получатель', related_name='to', null=True)
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(max_length=400, db_index=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Author: {}, to: {}, title: {}".format(self.author, self.recipient, self.title)

    def get_author(self):
        return reverse('profile_detail_url', kwargs={'pk':self.author.id})

    def get_to(self):
        return reverse('profile_detail_url', kwargs={'pk': self.recipient.id})



# class Chat(models.Model):
#     pass