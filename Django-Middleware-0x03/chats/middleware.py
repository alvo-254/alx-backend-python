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
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_start_time = time(9, 0, 0)   # 9 AM
        self.allowed_end_time = time(17, 0, 0)    # 5 PM

    def __call__(self, request):
        current_time = datetime.now().time()
        if request.path.startswith('/api/') and not (self.allowed_start_time <= current_time <= self.allowed_end_time):
            return JsonResponse({'error': 'Chat access is only allowed between 9 AM and 5 PM.'}, status=403)

        return self.get_response(request)


class RolePermissionMiddleware:
    """
    Restricts access based on user role.
    Only allows users with role 'user', 'moderator', or 'admin'.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            user = getattr(request, 'user', None)
            if user is not None and user.is_authenticated:
                if user.role not in ['user', 'moderator', 'admin']:
                    return JsonResponse({'error': 'Access denied: insufficient role'}, status=403)

        return self.get_response(request)
