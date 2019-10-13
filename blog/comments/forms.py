from .models import Comment
from django import forms


class CommentAddForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'author', 'post']
        labels = {
            'text': 'Напишите:'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control', 'style':'height:100px'}),
            'author': forms.HiddenInput(),
            'post': forms.HiddenInput()
        }