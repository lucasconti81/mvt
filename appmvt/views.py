from django.shortcuts import render
from appmvt.models import Familiar as fm
from django.http import HttpResponse
import datetime
from django.template import Template,Context,loader

def mostrarfamiliar(self):
    familia=fm(numero=1,nombre="Juan",apellido="perez",email="jp@pepe",fecha="2022-08-07")
    familia.save()
    familia2=fm(numero=2,nombre="Ana",apellido="dias",email="ad@gmail",fecha="2022-08-09")
    familia2.save()
    familia3=fm(numero=3,nombre="Esteban",apellido="quito",email="eq@gmail",fecha="2022-08-10")
    familia3.save()

    numeros=[familia.numero,familia2.numero,familia3.numero]
    nombres=[familia.nombre,familia2.nombre,familia3.nombre]
    apellidos=[familia.apellido,familia2.apellido,familia3.apellido]
    emails=[familia.email,familia2.email,familia3.email]
    fechas=[familia.fecha,familia2.fecha,familia3.fecha]
    diccionario={"numero":numeros,"nombre":nombres,"apellido":apellidos,"email":emails,"fecha":fechas}

    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)
