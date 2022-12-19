from django.urls import path 
from .views import *

urlpatterns = [
    path("jugadores/", jugadores,name="jugadores"),
    path("equipos/", equipos,name="equipos"),
    path("estadios/", estadios,name="estadios"),
    
    path("", home,name="home"),
    
    path("jugadorForm/", jugadorForm, name="jugadorForm"),
    path("estadioForm/", estadioForm, name="estadioForm"),
    path("equipoForm/", equipoForm, name="equipoForm"),
    
    path("buscarJugador/", buscarJugador, name="buscarJugador" ),
    path("buscar/", buscar, name="buscar" ),
    path("resultadoBuscador/", resultadoBuscador,name="resultadoBuscador"),
]
