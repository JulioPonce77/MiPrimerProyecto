from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserAuthentication(AbstractUser):
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.email

