from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)