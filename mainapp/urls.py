# mainapp/urls.py
from django.urls import path
from .views import home, redirect_url, all_urls, register_view, login_view, logout_view, edit_url, delete_url

urlpatterns = [
    path('', home, name='home'),
    path('all/', all_urls, name='all_urls'),
    path('s/<str:url>/', redirect_url, name='redirect'),
    
    # Auth
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Edit/Delete
    path('edit/<int:url_id>/', edit_url, name='edit_url'),
    path('delete/<int:url_id>/', delete_url, name='delete_url'),
]
