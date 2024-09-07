# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    physical_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups',  # Add a unique related name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',  # Add a unique related name
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'physical_address', 'phone_number']

    username = None







from django.db import models
from django.conf import settings

class Animal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    species = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=100)
    production_purpose = models.CharField(max_length=100)
    about_animal = models.TextField()
 
