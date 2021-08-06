from django import forms
from django.contrib.auth.models import User
from app_five.models import Userprofileinfo

class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class Userprofileinfoform(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields = ('portfolio_site','profile_pic')
