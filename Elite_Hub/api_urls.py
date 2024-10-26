# app_name/api_urls.py
from django.urls import path
from .views import register_user, UsuarioListView, upload_image

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('usuarios/', UsuarioListView.as_view(), name='usuarios'),
    path('upload_image/', upload_image, name='upload_image'),
]
