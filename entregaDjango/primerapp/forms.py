from django import forms
YEARS= [x for x in range(1900,2022)]

#Estos los hace DJANGO unchained

class JugadorForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=15)
    apellido= forms.CharField(label="Apellido", max_length=15)
    edad= forms.IntegerField(label="Edad")
    posicion= forms.CharField(label="Posicion", max_length=15)
    equipo= forms.CharField(label="Equipo", max_length=15)
    
class EquipoForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=15)
    apodo= forms.CharField(label="Apodo", max_length=15)
    titulosInternacionales= forms.IntegerField(label="Titulos internacionales")
    fundacion= forms.DateField(label="Fecha de fundacion", initial="1900-01-01", widget=forms.SelectDateWidget(years=YEARS))
