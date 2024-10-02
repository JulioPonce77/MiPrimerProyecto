from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .models import CustomUserAuthentication

# Vista para el inicio de sesión personalizado
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

# Vista para la autenticación mediante token
class CustomAuthTokenView(APIView):
    def post(self, request):
        email = request.data.get('email')  # Cambia 'username' a 'email'
        password = request.data.get('password')
        
        print(email)
        print(password)
        
        user = authenticate(request, email=email, password=password)  
        print(user)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
