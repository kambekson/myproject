from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_of_birth = models.DateField(null=True, blank=False)  # Изменено на blank=False
    profile_picture = models.ImageField(default='fallback.png', blank=True)
    first_name = models.CharField(max_length=30, blank=False)  # Изменено на blank=False
    last_name = models.CharField(max_length=30, blank=False)  # Изменено на blank=False

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth', 'first_name', 'last_name']  # Добавлено first_name и last_name

    def __str__(self):
        return self.username
