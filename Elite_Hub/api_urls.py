from django.urls import path
from .views import  UsuarioListView, UsuarioCreateView, NutricionistaCreateView
from .views import NutricionistaListView, DeportistaListView, PatrocinadorListView, MarcaListView, PqrsListView, ContenidoListView
from .views import RegisterUser, ParametrosListView
urlpatterns = [

 #Usuarios
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario-create'),

#Nutricinistas
    path('nutricionistas/', NutricionistaListView.as_view(), name='nutricionistas_list'),
    path('nutricionistas/create/', NutricionistaCreateView.as_view(), name='nutricionistas_list'),

#Deportistas
    path('deportistas/', DeportistaListView.as_view(), name='deportistas_list'),

#Patrocinadores
    path('patrocinadores/',PatrocinadorListView.as_view(), name='patrocinadres_list'),

#Marcas
    path('marcas/',MarcaListView.as_view(), name='marcas_list'),

#Register
    path('register/',RegisterUser.as_view(), name='register'),

#Otras URLs
    path('pqrs/',PqrsListView.as_view(), name='pqrs_list'),
    path('contenidos/',ContenidoListView.as_view(), name='contenidos_list'),
    path('parametros/',ParametrosListView.as_view(), name='parametros'),


]
