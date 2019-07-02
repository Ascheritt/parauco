from django.db import models
#from tablero.models import Tablero

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length =200)

    def __str__(self):
        return self.categoria

class Indicador(models.Model):
    nombre_kpi = models.CharField(max_length=200)
    #formula = models.CharField(max_length=200)
    meta_kpi = models.IntegerField()
    categoria = models.ForeignKey(Categoria, null=True,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombre_kpi


class Info_kpi(models.Model):
    valor_kpi = models.IntegerField()
    fecha_modificacion = models.DateField(['%d/%m/%Y'])
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    






   
