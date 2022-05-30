
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader
from app_coder.models import Familiar

def template_using_context(
    self, name: str = 'Name', last_name: str = 'Last_name'):

    miHtml = open('C:/Users/Jaime/Desktop/DJANGO_2/live_class/live_class/templates/template.html')
    template = Template(miHtml.read())
    miHtml.close()

    context_dict = {
        'name': name,
        'last_name': last_name,
    }

    my_context = Context(context_dict)
    render = template.render(my_context)
    return HttpResponse(render)

def template_using_loader(
    self, name: str = 'Name', last_name: str = 'Last_name'):
    template = loader.get_template('template_loader.html')

def new_familiar(
    self, nombre:str = 'nombre', edad: int = 'edad', fecha_de_nacimiento: date = 'fecha_de_nacimiento'):

    template = loader.get_template('new_familiar.html')

    familiar = Familiar(nombre = nombre, edad = edad, fecha_de_nacimiento = fecha_de_nacimiento)

    familiar.save()

    context_dict = {
        'familiar': familiar
    }

    render = template.render(context_dict)

    return HttpResponse(render)

def def_template(self):
    template = loader.get_template('def_template.html')

    render = template.render()

    return HttpResponse(render)

def familiar_info(request):
    fami = Familiar.objects.all()
    print("myoutput", fami)
    return render(request, 'C:/Users/Jaime/Desktop/DJANGO_2/live_class/live_class/templates/familiar_info.html', {'fam':fami})

