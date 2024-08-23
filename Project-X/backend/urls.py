from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import TestCSRFToken  # Remove GetCSRFToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', views.ping, name='ping'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('simple-post/', views.simple_post, name='simple_post'),
    # Remove the following line
    # path('get-csrf-token/', GetCSRFToken.as_view(), name='get_csrf_token'),
    path('test-csrf-token/', TestCSRFToken.as_view(), name='test_csrf_token'),
]