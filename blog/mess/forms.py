from django import forms
from .models import Message



class MessageCreateForm1(forms.ModelForm):


    class Meta:
        model= Message
        fields = ['author', 'recipient', 'title', 'body']

        widgets = {
            'author': forms.HiddenInput(),
            'recipient': forms.HiddenInput()
        }


class MessageCreateForm2(forms.ModelForm):


    class Meta:
        model= Message
        fields = ['author', 'recipient', 'title', 'body']

        widgets = {
            'author': forms.HiddenInput()
        }