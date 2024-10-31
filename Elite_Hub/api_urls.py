from django.urls import path
from .views import register_user, UsuarioListView
from .views import NutricionistaListView, DeportistaListView, PatrocinadorListView, MarcaListView, PqrsListView, ContenidoListView

urlpatterns = [

    path('register/', register_user, name='register_user'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('nutricionistas/', NutricionistaListView.as_view(), name='nutricionistas_list'),
    path('deportistas/', DeportistaListView.as_view(), name='deportistas_list'),
    path('patrocinadores/',PatrocinadorListView.as_view(), name='patrocinadres_list'),
    path('marcas/',MarcaListView.as_view(), name='marcas_list'),
    path('pqrs/',PqrsListView.as_view(), name='pqrs_list'),
    path('contenidos/',ContenidoListView.as_view(), name='contenidos_list'),


]
