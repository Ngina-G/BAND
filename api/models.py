from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=32)
    notes = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
