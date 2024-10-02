from django.urls import path
from .views import (
    PaisListView, 
    PaisCreateView, 
    PaisUpdateView, 
    PaisDeleteView,
    DepartamentoListView, 
    DepartamentoCreateView, 
    DepartamentoUpdateView, 
    DepartamentoDeleteView,
    MunicipioListView, 
    MunicipioCreateView, 
    MunicipioUpdateView, 
    MunicipioDeleteView, 
    SignUpView
)
from django.contrib.auth.views import LoginView, LogoutView  # Importar LoginView y LogoutView

urlpatterns = [
    # URLs para País
    path('pais/', PaisListView.as_view(), name='pais_list'),
    path('pais/add/', PaisCreateView.as_view(), name='pais_add'),
    path('pais/<int:pk>/edit/', PaisUpdateView.as_view(), name='pais_edit'),
    path('pais/<int:pk>/delete/', PaisDeleteView.as_view(), name='pais_delete'),

    # URLs para Departamento
    path('departamento/', DepartamentoListView.as_view(), name='departamento_list'),
    path('departamento/add/', DepartamentoCreateView.as_view(), name='departamento_add'),
    path('departamento/<int:pk>/edit/', DepartamentoUpdateView.as_view(), name='departamento_edit'),
    path('departamento/<int:pk>/delete/', DepartamentoDeleteView.as_view(), name='departamento_delete'),

    # URLs para Municipio
    path('municipio/', MunicipioListView.as_view(), name='municipio_list'),
    path('municipio/add/', MunicipioCreateView.as_view(), name='municipio_add'),
    path('municipio/<int:pk>/edit/', MunicipioUpdateView.as_view(), name='municipio_edit'),
    path('municipio/<int:pk>/delete/', MunicipioDeleteView.as_view(), name='municipio_delete'),

    # URL para registro
    path('signup/', SignUpView.as_view(), name='signup'),  

    # URLs de autenticación
    path('login/', LoginView.as_view(), name='login'),  # URL para iniciar sesión
    path('logout/', LogoutView.as_view(), name='logout'),  # URL para cerrar sesión
]
