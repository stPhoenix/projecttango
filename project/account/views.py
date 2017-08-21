from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Account
from django.urls import reverse
from django.db.models import ObjectDoesNotExist
from .forms import SettingsAccountForm
from social_django.models import UserSocialAuth

# Create your views here.


class Settings(LoginRequiredMixin, generic.UpdateView):
    model = Account
    template_name = 'account/settings.html'
    success_url = '#'
    fields = ['username', 'first_name', 'last_name', 'avatar']

    def get_context_data(self, **kwargs):
        context = super(Settings, self).get_context_data()
        user = context['object']
        try:
            google_login = user.social_auth.get(provider='google-oauth2')
        except UserSocialAuth.DoesNotExist:
            google_login = None

        try:
            vk_login = user.social_auth.get(provider='vk-oauth2')
        except UserSocialAuth.DoesNotExist:
            vk_login = None
        try:
            facebook_login = user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            facebook_login = None

        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

        context['google_login'] = google_login
        context['vk_login'] = vk_login
        context['facebook_login'] = facebook_login
        context['can_disconnect'] = can_disconnect

        return context

    def form_valid(self, form):
        print('Form is valid')
        return super(Settings, self).form_valid(form)

    def form_invalid(self, form):
        print('Form is invalid')
        return super(Settings, self).form_invalid(form)


