from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import User, Cart, Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address']


class ContactFrom(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']

# class BuyForm(forms.ModelForm):
#     class Meta:
#         model = Buy
#         fields = ['number', 'phone_number', 'name']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'phone']

    def is_valid(self, data=None, raise_exception=True):
        if User.objects.filter(username=data['username']).exists():
            return False
        else:
            return True

    def save(self, commit=True):
        username = self.data['username']
        password = self.data['password1']
        phone = self.data['phone']

        user = User.objects.create(
            username=username,
            phone=phone
        )
        user.set_password(password)
        user.save()
        return user
