from django import forms
from .models import Indicador, Info_kpi, Categoria

class IndicadorForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = [
            'nombre_kpi',
            'meta_kpi',
            'categoria',
            #'info',
        ]
        

        labels = {
            'nombre_kpi':'Nombre del Indicador',
            'meta_kpi':'Meta Indicador',
            'categoria': 'Categoria Indicador',
            #'info':'Informacion NULL',

        }
        widgets = {
            'nombre_kpi': forms.TextInput(),
            'meta_kpi': forms.TextInput(),
            'categoria': forms.Select(),
        }

class InformacionForm(forms.ModelForm):
    class Meta:
        model = Info_kpi
        fields = [
            'valor_kpi',
            'fecha_modificacion',
            'indicador',
        ]
        labels = {
            'valor_kpi':'Valor del Indicador',
            'fecha_modificacion':'Fecha',
            'indicador':'Codigo Indicador',
        }
        widgets = {
            'valor_kpi': forms.NumberInput(),
            'fecha_modificacion': forms.DateTimeInput(),
            'indicador': forms.RadioSelect(attrs={'required': True}),
        }

class Informacion(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = [
            'nombre_kpi',
            'meta_kpi',
            'categoria',
        ]
        labels = {
            'valor_kpi':'Valor del Indicador',
            'fecha_modificacion':'Fecha',
            #'id_indicador':'Codigo Indicador',
        }
        widgets = {
            'nombre_kpi': forms.TextInput(),
            'meta_kpi': forms.NumberInput(attrs={'minlength':0, 'maxlength':999, 'required':True}),
            #'id_indicador': forms.SelectMultiple(),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields = [
            'categoria',
        ]
        labels = {
            'categoria':'Seleccione Categoria',
        }
        widgets = {
            'categoria': forms.Select(),
        }