from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=124)
    about = models.CharField(max_length=255)

class User(AbstractUser):
    desc =models.CharField(max_length=255)