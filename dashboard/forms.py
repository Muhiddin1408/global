from django import forms
from bloc.models import User, Product


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'phone', 'status',)


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description')


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'type']
