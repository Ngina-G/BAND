from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class User(AbstractUser):
    username = models.CharField(db_index=True,max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(blank=True,default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    email_address = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return f'{self.user.username} Profile' 
    
    @classmethod
    def update_profile(cls, id, value):
        cls.objects.filter(id=id).update(image=value)


class Notes(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notes',null=True)
    NoteId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    notes = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)