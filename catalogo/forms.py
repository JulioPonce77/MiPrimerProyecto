from django import forms
from .models import Pais, Departamento, Municipio

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'pais']

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombre', 'departamento']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)