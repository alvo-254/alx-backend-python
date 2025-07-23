# chats/middleware.py
from datetime import datetime

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
