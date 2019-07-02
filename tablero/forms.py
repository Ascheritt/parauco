from django import forms
from .models import Tablero

class TableroForm(forms.ModelForm):
    class Meta:
        model = Tablero
        fields = [
            'nombre_tablero',
            'fecha',
            'indicador',
        ]

        labels = {
            'nombre_tablero':'Nombre del Tablero',
            'fecha': 'Fecha',
            'indicador':'Seleccione Indicadores',
        }
        widgets = {
            'nombre_tablero': forms.TextInput(),
            'fecha': forms.TextInput(),
            'indicador': forms.CheckboxSelectMultiple(),
            
        }


