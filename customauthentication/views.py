from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomLoginForm  # Asegúrate de importar el CustomLoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  
    authentication_form = CustomLoginForm  # Usa el formulario de inicio de sesión personalizado

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')  # Redirige a home después de cerrar sesión

class CustomAuthTokenView(APIView):
    def post(self, request):
        email = request.data.get('email')  
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  
    template_name = 'registration/signup.html' 
    success_url = reverse_lazy('login')  

