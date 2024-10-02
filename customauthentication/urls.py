from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView  

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),   
    path('api-token-auth/', CustomAuthTokenView.as_view(), name='api_token_auth'),  
]
