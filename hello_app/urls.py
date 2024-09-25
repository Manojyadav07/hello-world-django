from django.urls import path
from .views import hello_world  # Import the hello_world view function

urlpatterns = [
    path('hello/', hello_world),  # Define the 'hello/' route, mapped to hello_world view
]
