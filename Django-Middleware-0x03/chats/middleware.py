import re
from datetime import datetime, time
from django.http import JsonResponse

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


class TimeAccessRestrictionMiddleware:
    """
    Allows access only between 8:00 AM and 5:00 PM server time.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.start_time = time(8, 0, 0)
        self.end_time = time(17, 0, 0)

    def __call__(self, request):
        now = datetime.now().time()
        if not (self.start_time <= now <= self.end_time):
            return JsonResponse({'error': 'Access allowed only between 08:00 and 17:00.'}, status=403)

        return self.get_response(request)


class RolePermissionMiddleware:
    """
    Only users with roles 'moderator' or 'admin' can post messages.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/') and request.method == 'POST':
            user = request.user
            if not user.is_authenticated:
                return JsonResponse({'error': 'Authentication required.'}, status=401)

            if getattr(user, 'role', None) not in ['moderator', 'admin']:
                return JsonResponse({'error': 'You do not have permission to perform this action.'}, status=403)

        return self.get_response(request)


class OffensiveLanguageMiddleware:
    """
    Middleware to detect offensive words in message content.
    Blocks request if offensive language is found in POST body.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.offensive_words = ["badword", "nasty", "stupid"]

    def __call__(self, request):
        if request.path.startswith('/api/') and request.method == 'POST':
            try:
                body = request.body.decode('utf-8')
                for word in self.offensive_words:
                    if re.search(rf'\b{word}\b', body, re.IGNORECASE):
                        return JsonResponse({'error': 'Offensive language is not allowed.'}, status=400)
            except Exception:
                return JsonResponse({'error': 'Invalid request body.'}, status=400)

        return self.get_response(request)
