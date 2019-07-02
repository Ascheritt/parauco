from django.db import models
from indicador.models import Indicador
# Create your models here.


class Tablero(models.Model):
    nombre_tablero = models.CharField(max_length=200)
    fecha  = models.CharField(max_length=10)
    indicador = models.ManyToManyField(Indicador, blank=True)
    
    def __str__(self):
        return self.nombre_tablero

