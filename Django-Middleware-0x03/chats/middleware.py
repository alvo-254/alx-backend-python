# chats/middleware.py
from datetime import datetime, timedelta
from django.http import JsonResponse
from collections import defaultdict, deque

# Dictionary to store requests per IP
request_log = defaultdict(lambda: deque())

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 5  # messages
        self.time_window = timedelta(minutes=1)  # per minute

    def __call__(self, request):
        if request.method == "POST" and request.path.startswith("/api/messages"):
            ip = self.get_client_ip(request)
            now = datetime.now()

            # Remove outdated entries
            while request_log[ip] and now - request_log[ip][0] > self.time_window:
                request_log[ip].popleft()

            if len(request_log[ip]) >= self.rate_limit:
                return JsonResponse(
                    {"error": "Rate limit exceeded. Max 5 messages per minute."},
                    status=429
                )

            request_log[ip].append(now)

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR', '')
        return ip
