from django import forms
from rango.models import User,Game,Forum

class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter Username: ")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial =0)
    likes = forms.IntegerField(widget = forms.HiddenInput(),initial=0)


    class Meta:
        model = User
        fields = ('name','views','likes')
