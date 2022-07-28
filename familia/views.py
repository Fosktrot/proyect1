from multiprocessing import context
from django.shortcuts import render
from familia.models import familia
# Create your views here.

def create_famili(request):
    new_familia = familia.objects.create(nombre = "elon musk" , edad = "90" , nacimiento ="" )
    new_familia = familia.objects.create(nombre = "lol" , edad = "23" , nacimiento ="" )
    new_familia = familia.objects.create(nombre = "juna" , edad = "9" , nacimiento ="" )
    context = {
        "new_familia" : new_familia
    }

    return render(request, "new_familia.html", context=context)

def list_famili(request):
    familiares = familia.objects.all()
    context = {
        "familiares":familiares
    }
    return render(request, "lista_familia.html", context=context)