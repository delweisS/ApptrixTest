from django.urls import path

from .views import signup_view

urlpatterns = [
    # Signup view
    path('signup/', signup_view, name='signup'),
]
