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
        # Keep "widgets" for a case; it regulates behaviour of a form
        """widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Please, enter username', "class": "col-6 d-inline-flex flex-column my-2 ml-1",}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Please, enter password', 'class': "col-6 d-inline-flex flex-column my-2 ml-1"}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Please, enter your first name', "class": "col-6 d-inline-flex flex-column my-2 ml-1"}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Please, enter your last name', "class": "col-6 d-inline-flex flex-column my-2 ml-1"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Please, enter your E-mail', "class": "col-6 d-inline-flex flex-column my-2 ml-1"}),
        }"""
