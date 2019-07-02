from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Indicador, Info_kpi, Categoria
from .forms import IndicadorForm, InformacionForm, CategoriaForm
from django.contrib.auth import logout
import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    #visitas=request.session.get('visitas',0)
    #request.session['visitas'] = visitas + 1
    day  = timezone.now()
    fecha  = day.strftime("%Y/%m/%d")
    return render(request,'indicador/index.html', context={'fecha':fecha})

def indexadmin(request):
    #visitas=request.session.get('visitas',0)
    #request.session['visitas'] = visitas + 1
    day  = timezone.now()
    fecha  = day.strftime("%Y/%m/%d")
    return render(request,'indicador/indexadmin.html', context={'fecha':fecha})

class IndicadorCrear(CreateView):
    model = Indicador
    form_class = IndicadorForm
    template_name = 'indicador/crear_indicador.html'
    success_url = reverse_lazy('lista_indicador')

class IndicadorLista(ListView):
    model = Indicador
    template_name = 'indicador/lista_indicador.html'

class IndicadorActualizar(UpdateView):
    model = Indicador
    form_class = IndicadorForm
    template_name = 'indicador/crear_indicador.html'
    success_url = reverse_lazy('lista_indicador')

class IndicadorEliminar(DeleteView):
    model = Indicador
    form_class = IndicadorForm
    template_name = 'indicador/eliminar_indicador.html'
    success_url = reverse_lazy('lista_indicador')


#vistas Informacion KPI

class AñadirInformacion(CreateView):
    model = Info_kpi
    form_class = InformacionForm
    template_name = 'indicador/informacion_kpi.html'
    success_url = reverse_lazy('index')


def graficoview(request,pk):
    ind= Indicador.objects.filter(categoria=pk)
    return render(request,'indicador/grafico.html',{'ind':ind})

def graficoviewadmin(request,pk):
    ind= Indicador.objects.filter(categoria=pk)
    return render(request,'indicador/graficoadmin.html',{'ind':ind})

def Lista(request,pk):
    indicador=Indicador.objects.filter(id=pk)
    form = InformacionForm()
    return render(request,'indicador/informacion_kpi.html',{'indicador':indicador, 'form':form})


def Añadir(request,pk):
    if request.method == 'POST':
        form = InformacionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('indicador/lista_indicador.html')
    else:
        form = InformacionForm()
    return render(request,'indicador/informacion_kpi.html',{'form':form})

def Cerrar_sesion(request):
    logout(request)
    return redirect(request,'indicador/grafico.html')

def ILista(request):
    day  = timezone.now()
    fecha  = day.strftime("%Y-%m-%d")
    model = Info_kpi.objects.filter(fecha_modificacion=fecha)
    return render(request,'indicador/lista_indicador.html',{'model':model})

def Cuadro(request):
    form = Categoria.objects.all()
    return render(request,'indicador/cuadro.html',{'form':form})

def Cuadro(request):
    form = Categoria.objects.all()
    return render(request,'indicador/cuadroadmin.html',{'form':form})

class CuadroLista(ListView):
    model = Categoria
    template_name = 'indicador/cuadro.html'

class CuadroListaadmin(ListView):
    model = Categoria
    template_name = 'indicador/cuadroadmin.html'