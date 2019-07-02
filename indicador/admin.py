from django.contrib import admin
from indicador.models import Indicador, Info_kpi, Categoria
from tablero.models import Tablero
# Register your models here.

admin.site.register(Indicador)
admin.site.register(Categoria)
admin.site.register(Info_kpi)
admin.site.register(Tablero)
