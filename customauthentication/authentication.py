# customauthentication/authentication.py

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Obtén el token de autenticación de los encabezados
        token = request.META.get('HTTP_AUTHORIZATION')
        
        if not token:
            return None  # No se proporcionó un token
        
        try:
            # Aquí puedes agregar tu lógica para verificar el token
            user = User.objects.get(token=token)  # Supongamos que tienes un modelo que almacena tokens
        except User.DoesNotExist:
            raise AuthenticationFailed('Invalid token')
        
        # Si todo está bien, devuelve el usuario autenticado
        return (user, None)  # El segundo elemento es None porque no estamos usando un tipo de usuario adicional

