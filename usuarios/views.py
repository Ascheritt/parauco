from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from usuarios.forms import RegistroForm
from django.contrib.auth import authenticate, login
# Create your views here.

class RegistroUsuarios(CreateView):
    model = User
    template_name = "usuarios/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('index')


def Registro(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username= username,password= password)
            login(request, user)
            return redirect('index')
    
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render (request,'usuarios/registro.html', context)


def login_vista(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('index')
    
    else:
        return redirect('login')