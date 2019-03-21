
from django import forms
from django.contrib.auth.models import User
from dice.models import User, Game, UserProfile
from dice.models import User,Game
from dice.models import UserProfile



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
