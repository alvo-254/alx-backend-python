# chats/middleware.py
from datetime import datetime
import logging

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)
        self.logfile = 'requests.log'

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "AnonymousUser"
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}\n"
        with open(self.logfile, 'a') as f:
            f.write(log_entry)
        response = self.get_response(request)
        return response
