# chats/middleware.py

from datetime import datetime
import logging

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Set up a logger that writes to a file
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"User: {user} - Path: {request.path}"
        logging.info(log_message)

        response = self.get_response(request)
        return response
