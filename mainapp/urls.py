from django.urls import path
from .views import home, redirect_url, all_urls

urlpatterns = [
    path('', home, name='home'),
    path('all/', all_urls, name='all_urls'),
    path('s/<str:url>/', redirect_url, name='redirect'),  # added prefix 's/'
]
