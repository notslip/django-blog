from django import forms
from .models import Post


# class PostForm(forms.ModelForm):
#             title = forms.CharField(max_length=150)
#             body = forms.CharField(max_length=150)
#             slug = forms.SlugField(max_length=150)
#             tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
#
#             def save(self):
#                 new_post=Post.objects.create(
#                     title=self.cleaned_data['title'],
#                     body=self.cleaned_data['body'],
#                     slug=self.cleaned_data['slug'],
#                     tags=self.cleaned_data['tags'],
#                 )


class PostCreateForm(forms.ModelForm):

      class Meta:
          model = Post
          fields = ['title', 'slug', 'body', 'tags', 'author']
          widgets = {
              'author': forms.HiddenInput()
          }
