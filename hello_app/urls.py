from django.urls import path
from .views import hello_world, hello_world_html

urlpatterns = [
    path('hello/', hello_world),  # JSON response
    path('hello_html/', hello_world_html),  # HTML response
]
