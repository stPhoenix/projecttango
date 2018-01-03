from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

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
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username', "class": "d-inline-flex mx-2 my-1 form-control",}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': "d-inline-flex mx-2 my-1 form-control"}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name', "class": "d-inline-flex mx-2 my-1 form-control"}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name', "class": "d-inline-flex mx-2 my-1 form-control"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your E-mail', "class": "d-inline-flex mx-2 my-1 form-control"}),
        }
