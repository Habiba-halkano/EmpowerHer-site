from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('advocate', 'Advocate'),
        ('survivor', 'Survivor'),
        ('general', 'General User'),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='general')


