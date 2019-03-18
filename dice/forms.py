
from django import forms
from dice.models import User, Game, UserProfile

from dice import forms
from dice.models import User,Game

from dice.models import UserProfile



class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=128,help_text="Please enter Username: ")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial =0)
    likes = forms.IntegerField(widget = forms.HiddenInput(),initial=0)
    password = forms.CharField(widget=forms.PasswordInput())
    

    class Meta:
        model = User
        fields = ('name','views','likes','password')

class UserProfileForm(forms.ModelForm):

    picture = forms.ImageField(required=False)
    bio = forms.CharField(max_length=800,help_text="Please tell us about yourself?: ")
    player_endorsments = forms.IntegerField(widget = forms.HiddenInput(),initial=0)
    game_list = forms.CharField(max_length=800,help_text="Please tell us about the games you like to play?:")
    class Meta:
        model = UserProfile
        fields = ('picture','bio','player_endorsments','game_list',)
        exclude = ('user',)

