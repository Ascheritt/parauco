from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tablero
from .forms import TableroForm
from django.contrib.auth import logout
# Create your views here.

#Vistas Tablero

class TableroLista(ListView):
    model = Tablero
    template_name = 'tablero/lista_kpi_tablero.html'

def Lista(request):
    form = Tablero.objects.all()
    return render(request,'tablero/lista_kpi_tablero.html',{'form':form})

class TableroCrear(CreateView):
    model = Tablero
    form_class = TableroForm
    template_name = 'tablero/crear_tablero.html'
    success_url = reverse_lazy('lista_tablero')

class TableroActualizar(UpdateView):
    model = Tablero
    form_class = TableroForm
    template_name = 'tablero/crear_tablero.html'
    success_url = reverse_lazy('lista_tablero')

class TableroEliminar(DeleteView):
    model = Tablero
    form_class = TableroForm
    template_name = 'tablero/eliminar_tablero.html'
    success_url = reverse_lazy('lista_tablero')


def Añadir_kpi_tablero(request):
    if request.method =='POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('lista_tablero')
    else:
        form = TableroForm()
    return render(request, 'tablero/crear_kpi_tablero.html', {'form':form})


