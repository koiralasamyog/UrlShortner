from django.urls import path
from .views import home, redirect_url

urlpatterns = [
        path('',home, name='home'),
        path('<str:url>/', redirect_url, name='redirect'),
]
