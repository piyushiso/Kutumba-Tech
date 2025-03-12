# middleware.py: Custom middleware to enforce authentication checks globally.

from django.shortcuts import redirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path in ['/login/', '/register/']:
            return redirect('dashboard')
        elif not request.user.is_authenticated and request.path == '/dashboard/':
            return redirect('login')
        return self.get_response(request)