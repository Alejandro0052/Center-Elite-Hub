"""
URL configuration for Elite_Hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views  
#from .views import register_user
from .views import RegisterUser, LoginView
#from .views import  #register_user, upload_image, UsuarioListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/register/', RegisterUser.as_view(), name='register_user'),
    path('', views.home, name='home'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('api/', include('Elite_Hub.api_urls')), 
    path('reporte_usuarios/', views.reporte_usuarios, name='reporte_usuarios'),
   # path('admin/reporte-datos/', views.reporte_datos_admin, name='reporte_datos_admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)