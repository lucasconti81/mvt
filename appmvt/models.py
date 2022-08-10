from django.db import models

class Familiar(models.Model):

    numero = models.IntegerField()
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    fecha = models.DateField() 