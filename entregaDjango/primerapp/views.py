from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from primerapp.forms import *
# Create your views here. objetos. def, request


def jugadores(request):
    return render(request, "../Templates/jugadores.html")

def equipos(request):
    return render(request, "..\Templates\equipos.html")

def estadios(request):
    return render(request, "..\Templates\estadios.html")

def home(request):
    return render(request, "..\Templates\home.html")
#----------------------------------------------------------------
#----------------------------------------------------------------
def estadioForm(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        apodo=request.POST["apodo"]
        fundacion=request.POST["fundacion"]
        estadio=Estadio(nombre=nombre, apodo=apodo, fundacion=fundacion)
        estadio.save()
        return render(request, "..\Templates\home.html", {"mensaje":"GUARDADO!"})
    else:
        return render(request, "..\Templates\estadioForm.html")
    
    

def jugadorForm(request):
    if request.method=="POST":
        formulario= JugadorForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            edad=info["edad"]
            posicion=info["posicion"]
            equipo=info["equipo"]
            jugador=Jugador(nombre=nombre, apellido=apellido,edad=edad,posicion=posicion,equipo=equipo)
            jugador.save()
            return render(request, "..\Templates\home.html", {"mensaje":"GUARDADO!"})
    else:
        formulario=JugadorForm()
        return render(request, "..\Templates\jugadorForm.html", {"formulario":formulario})

def equipoForm(request):
    if request.method=="POST":
        formulario= EquipoForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            nombre=info["nombre"]
            apodo=info["apodo"]
            titulosInternacionales=info["titulosInternacionales"]
            fundacion=info["fundacion"]
            equipo=Equipo(nombre=nombre, apodo=apodo,titulosInternacionales=titulosInternacionales,fundacion=fundacion)
            equipo.save()
            return render(request, "..\Templates\home.html", {"mensaje":"GUARDADO!"})
    else:
        formulario=EquipoForm()
        return render(request, "..\Templates\equipoForm.html", {"formulario":formulario})
#----------------------------------------------------------------
#----------------------------------------------------------------

def buscarJugador(request):
    return render(request, "../Templates/buscarJugador.html")

def buscar(request):
    nombre= request.GET["nombre"]
    if nombre!="":
        jugadores= Jugador.objects.filter(nombre=nombre)
        return render(request, "../Templates/resultadoBuscador.html", {"jugadores": jugadores})
    else:
        return render(request, "../Templates/buscarJugador.html", {"mensaje": "Error, no se ingreso ningun Jugador!"})

def resultadoBuscador(request):
    return render(request, "../Templates/resultadoBuscador.html")