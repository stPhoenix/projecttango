from django import forms
from django.contrib.auth.models import User


class SettingsAccountForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)
    pk = forms.IntegerField(widget=forms.HiddenInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')