from django.shortcuts import render
from .models import Familia
# Create your views here.

def mostrar_familia(request):
    primo = Familia(nombre='Angel',apellido='Di Maria', edad='32', nacimiento='14/03/1990')
    tio = Familia(nombre='Dibu',apellido='Martinez', edad= '40', nacimiento='01/09/1980')
    sobrino = Familia(nombre='Lionel',apellido='Messi', edad='30', nacimiento='27/01/1992')
    return render(request, 'mostrar_familiar/mostrar_familiar.html', {'parientes': [primo, tio, sobrino]})
