#urls para el modulo de customauthentication

from django.urls import path
from .views import SignUpView, CustomAuthTokenView  # Asegúrate de que la vista esté importada

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api-token-auth/', CustomAuthTokenView.as_view(), name='api_token_auth'),  # Esta línea se queda aquí
]

