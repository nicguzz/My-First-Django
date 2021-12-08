from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def saludo(request): #primera vista

    name = "Nic"

    # templates_loader = loader.get_template("miplantilla.html")
    # doc_externo = open("/Users/nicguzzetti/Desktop/Clase/GitHub/Django/Hotelproj/Hotelproj/templates/miplantilla.html")

    # plt=Template(doc_externo.read())

    # doc_externo.close()

    # ctx=Context({"nombre_persona": name})

    # documento = templates_loader.render({"nombre_persona": name})

    return render(request, "miplantilla.html", {"nombre_persona": name})

def bye(request):
    return HttpResponse("Adeu Andreu")