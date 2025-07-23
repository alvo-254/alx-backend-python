from datetime import datetime
from django.http import JsonResponse
import datetime as dt


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


class TimeBasedAccessMiddleware:
    """
    Restrict access to chat endpoints after 5 PM server time (17:00).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/') and dt.datetime.now().hour >= 17:
            return JsonResponse(
                {'error': 'Access to chat is restricted after 5 PM.'},
                status=403
            )
        return self.get_response(request)


class RolepermissionMiddleware:
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
