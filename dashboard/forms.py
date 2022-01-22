from django import forms
from bloc.models import User


class UserUpdateForm(forms.ModelForm):
     class Meta:
         model = User
         fields = (
             'username',
             'phone',
             'status',
         )
