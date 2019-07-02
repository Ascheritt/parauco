from django.conf.urls import url
from usuarios.views import RegistroUsuarios
from . import views

urlpatterns =[
    #url('registro', RegistroUsuarios.as_view(), name="registro"),
    url('registro', views.Registro, name="registro"),
    #url('login2', views.login_vista, name="login2"),
]