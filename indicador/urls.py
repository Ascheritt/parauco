from django.urls import path
from .views import *
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index', login_required(views.index), name='index'),
    path('', login_required(views.indexadmin), name='indexadmin'),
    path('crear_indicador/', login_required(IndicadorCrear.as_view()), name='crear_indicador'),
    path('lista_indicador/', login_required(IndicadorLista.as_view()), name='lista_indicador'),
    path('editar_indicador/<int:pk>/', login_required(IndicadorActualizar.as_view()), name='editar_indicador'),
    path('eliminar_indicador/<int:pk>', login_required(IndicadorEliminar.as_view()), name='eliminar_indicador'),
    #path('',login_required(views.Cerrar_sesion), name='index'),

    path('informacion_kpi/', login_required(AñadirInformacion.as_view()), name='informacion_kpi'),
    path('grafico/<int:pk>', login_required(graficoview), name='grafico'),
    path('cuadro/', login_required(CuadroLista.as_view()), name='cuadro'),
    path('cuadroadmin/', login_required(CuadroListaadmin.as_view()), name='cuadroadmin'),
    path('graficoadmin/<int:pk>', login_required(graficoviewadmin), name='graficoadmin'),
]