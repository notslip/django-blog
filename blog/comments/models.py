from django.db import models
from user_profile.models import UserProfile
from blogengine.models import Post


class Comment(models.Model):

    text = models.TextField(max_length=500, verbose_name='Комментарий', db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comment', blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment', blank=True)

    def __str__(self):
        return 'Comment:{}, author:{}, post: {}'.format(self.text,
                                                        self.author.user.username,
                                                        self.post.title)

