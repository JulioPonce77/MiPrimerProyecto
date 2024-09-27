from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from .models import Pais, Departamento, Municipio
from .forms import PaisForm, DepartamentoForm, MunicipioForm, SearchForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'  
    success_url = reverse_lazy('login')  

class HomePageView(TemplateView):
    template_name = 'catalogo/home.html'  

# Pais Views
class PaisListView(ListView):
    model = Pais
    template_name = 'catalogo/pais_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Pais.objects.filter(Q(nombre__icontains=query))
        return Pais.objects.all()

class PaisCreateView(PermissionRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'catalogo/pais_form.html'
    success_url = reverse_lazy('pais_list')
    permission_required = 'catalogo.add_pais'

class PaisUpdateView(PermissionRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'catalogo/pais_form.html'
    success_url = reverse_lazy('pais_list')
    permission_required = 'catalogo.change_pais'

class PaisDeleteView(PermissionRequiredMixin, DeleteView):
    model = Pais
    template_name = 'catalogo/pais_confirm_delete.html'
    success_url = reverse_lazy('pais_list')
    permission_required = 'catalogo.delete_pais'

# Departamento Views
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'catalogo/departamento_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Departamento.objects.filter(Q(nombre__icontains=query))
        return Departamento.objects.all()

class DepartamentoCreateView(PermissionRequiredMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'catalogo/departamento_form.html'
    success_url = reverse_lazy('departamento_list')
    permission_required = 'catalogo.add_departamento'

class DepartamentoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'catalogo/departamento_form.html'
    success_url = reverse_lazy('departamento_list')
    permission_required = 'catalogo.change_departamento'

class DepartamentoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'catalogo/departamento_confirm_delete.html'
    success_url = reverse_lazy('departamento_list')
    permission_required = 'catalogo.delete_departamento'

# Municipio Views
class MunicipioListView(ListView):
    model = Municipio
    template_name = 'catalogo/municipio_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            return Municipio.objects.filter(Q(nombre__icontains=query))
        return Municipio.objects.all()

class MunicipioCreateView(PermissionRequiredMixin, CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'catalogo/municipio_form.html'
    success_url = reverse_lazy('municipio_list')
    permission_required = 'catalogo.add_municipio'

class MunicipioUpdateView(PermissionRequiredMixin, UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'catalogo/municipio_form.html'
    success_url = reverse_lazy('municipio_list')
    permission_required = 'catalogo.change_municipio'

class MunicipioDeleteView(PermissionRequiredMixin, DeleteView):
    model = Municipio
    template_name = 'catalogo/municipio_confirm_delete.html'
    success_url = reverse_lazy('municipio_list')
    permission_required = 'catalogo.delete_municipio'
