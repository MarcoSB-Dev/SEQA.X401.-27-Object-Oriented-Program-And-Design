from django.utils.deprecation import MiddlewareMixin

class DisableCSRFForCertainURLs(MiddlewareMixin):
    def process_request(self, request):
        if request.path in ['/get-csrf-token/']:  # Add your URL paths here
            setattr(request, '_dont_enforce_csrf_checks', True)