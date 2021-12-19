from django import forms
from .models import Post, SendMessage, Buy


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'title', 'user_name', 'price']


class ContactFrom(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = ['name', 'email', 'phone_number', 'message']

class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ['number', 'phone_number', 'name']
