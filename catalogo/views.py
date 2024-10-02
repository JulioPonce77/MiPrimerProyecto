from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from .models import Pais, Departamento, Municipio
from .forms import PaisForm, DepartamentoForm, MunicipioForm
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

# Home page view
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

# Sign Up View
class SignUpView(CreateView):
    form_class = UserCreationForm  
    template_name = 'registration/signup.html'  # Asegúrate de que el template existe
    success_url = reverse_lazy('login')  

# Custom Auth Token View
class CustomAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')  # Cambia 'username' a 'email'
        password = request.data.get('password')
        
        user = authenticate(username=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
