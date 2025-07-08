from django.urls import path
from .views import  UsuarioListView, UsuarioCreateView, NutricionistaCreateView, LoginView, NoticiasListView, EventosListView, TestimoniosListView
from .views import NutricionistaListView, DeportistaListView, PatrocinadorListView, MarcaListView, PqrsListView, ContenidoListView
from .views import RegisterUser, ParametrosListView, DeportistaCreateView, PatrocinadorCreateView, MarcaCreateView, PqrsCreateView, UsuariostiposListView

urlpatterns = [

#Usuarios unificados

    path('users/',  UsuariostiposListView.as_view(), name='usuriostipos_list'),


 #Usuarios
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario-create'),

#Nutricinistas
    path('nutricionistas/', NutricionistaListView.as_view(), name='nutricionistas_list'),
    path('nutricionistas/create/', NutricionistaCreateView.as_view(), name='nutricionistas_list'),

#Deportistas
    path('deportistas/', DeportistaListView.as_view(), name='deportistas_list'),
    path('deportistas/create/', DeportistaCreateView.as_view(), name='deportistas_list'),

#Patrocinadores
    path('patrocinadores/',PatrocinadorListView.as_view(), name='patrocinadres_list'),
    path('patrocinadores/create/',PatrocinadorCreateView.as_view(), name='patrocinadres_list'),

    

#Marcas
    path('marcas/',MarcaListView.as_view(), name='marcas_list'),
    path('marcas/create/',MarcaCreateView.as_view(), name='marcas_list'),

#Register
    path('register/',RegisterUser.as_view(), name='register'),

#Pqrs
    path('pqrs/',PqrsListView.as_view(), name='pqrs_list'),
    path('pqrs/create/',PqrsCreateView.as_view(), name='pqrs_list'),

#Otras URLs
    path('contenidos/',ContenidoListView.as_view(), name='contenidos_list'),
    path('parametros/',ParametrosListView.as_view(), name='parametros'),
    path('noticias/', NoticiasListView.as_view(), name='noticias'),
    path('eventos/', EventosListView.as_view(), name='eventos'),
    path('testimonios/',TestimoniosListView.as_view(), name='testimonios'),
    path('login/',LoginView.as_view(), name='login'),


]
