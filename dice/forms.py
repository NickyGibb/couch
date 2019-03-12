
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image','admin')

class EditProfileForm(UserProfileForm):
    template_name='/else'

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
