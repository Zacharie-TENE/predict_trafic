from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username  = forms.CharField(label="Nom d'utilisateur ")
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    phone  = forms.CharField(label="Téléphone ")
    address  = forms.CharField(label="Addresse ")
    image  = forms.ImageField(label="Photo de profil ")
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']
