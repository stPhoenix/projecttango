from django import forms


class SettingsAccountForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)
    pk = forms.IntegerField(widget=forms.HiddenInput)
