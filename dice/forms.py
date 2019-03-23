
from django import forms
from django.contrib.auth.models import User
from dice.models import User, Game, UserProfile
from dice.models import User,Game
from dice.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'

        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']


        if commit:
            user.save(
            )
        return User


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=128)
    email = forms.CharField(widget=forms.EmailInput())
    views = forms.IntegerField(widget = forms.HiddenInput(), initial =0)
    likes = forms.IntegerField(widget = forms.HiddenInput(),initial=0)
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username','email','views','likes','password')

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    bio = forms.CharField(max_length=800,help_text="Please tell us about yourself?: ")
    game_list = forms.CharField(max_length=800,help_text="Please tell us about the games you like to play?:")
    class Meta:
        model = UserProfile
        fields = ('picture','bio','game_list',)
        exclude = ('user',)
