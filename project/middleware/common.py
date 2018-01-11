import requests
import pytz

from django.utils import timezone


class TimezoneMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        user_time_zone = request.session.get('user_time_zone', None)
        if user_time_zone is None or user_time_zone == '' or user_time_zone == ' ':
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            freegeoip_response = requests.get('http://freegeoip.net/json/%s' % ip)
            freegeoip_response_json = freegeoip_response.json()
            user_time_zone = freegeoip_response_json['time_zone']
            if user_time_zone:
                request.session['user_time_zone'] = user_time_zone
        else:
            user_time_zone = timezone.get_current_timezone()
        timezone.activate(pytz.timezone(user_time_zone))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response