from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.views import View
from rest_framework import permissions
import logging


def ping(request):
    return JsonResponse({'message': 'pong'})

@require_POST
def add_to_cart(request):
    try:
        # Extract data from the request
        data = json.loads(request.body)
        print(data)
        # Log the data
        logging.info(f"Received data: {data}")
        
        # Return the data in the response
        return JsonResponse({'message': 'Item added to cart', 'data': data})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

@require_POST
def simple_post(request):
    # Your simple post logic here
    return JsonResponse({'message': 'Data posted successfully'})

class TestCSRFToken(View):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'CSRF token test'})

# Remove the GetCSRFToken class if it's no longer needed