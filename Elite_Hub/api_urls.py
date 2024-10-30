from django.urls import path
from .views import register_user, upload_image, UsuarioListView
from .views import NutricionistaListView
urlpatterns = [

    path('register/', register_user, name='register_user'),
    path('upload-image/', upload_image, name='upload_image'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('nutricionistas/', NutricionistaListView.as_view(), name='nutricionistas_list'),

]
