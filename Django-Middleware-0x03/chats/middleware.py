# chats/middleware.py
from datetime import datetime
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if hasattr(request, "user") and request.user.is_authenticated else "AnonymousUser"
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}\n"

        with open("requests.log", "a") as log_file:
            log_file.write(log_entry)

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        if not (6 <= current_hour < 21):  # 6AM to 9PM access only
            return HttpResponseForbidden("Access to chat is restricted outside 6 AM to 9 PM.")
        return self.get_response(request)
