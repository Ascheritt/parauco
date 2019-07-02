#from django.conf.urls import url
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required



urlpatterns =[
    path('crear_tablero/',login_required(TableroCrear.as_view()), name='crear_tablero'),
    #path('lista_kpi_tablero/',TableroLista.as_view(), name='lista_kpi_tablero'),
    path('lista_kpi_tablero/',login_required(Lista), name='lista_kpi_tablero'),
    path('editar_tablero/<int:pk>/',login_required(TableroActualizar.as_view()), name='editar_tablero'),
    path('eliminar_tablero/<int:pk>/',login_required(TableroEliminar.as_view()), name='eliminar_tablero'),
    

    #path('crear_kpi_tablero/',Kpi_tableroCrear.as_view(), name='crear_kpi_tablero'),  
   # path('crear_kpi_tablero/',IndicadorLista2.as_view(), name='lista_indicador2'),
]