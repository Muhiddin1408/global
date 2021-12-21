from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import SendMessage, User


# class PostCreateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['photo', 'title', 'user_name', 'price']
#

class ContactFrom(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = ['name', 'email', 'phone_number', 'number']

# class BuyForm(forms.ModelForm):
#     class Meta:
#         model = Buy
#         fields = ['number', 'phone_number', 'name']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']