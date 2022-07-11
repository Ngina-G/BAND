from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(db_index=True,max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.URLField(blank=True)
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    email_address = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile' 


