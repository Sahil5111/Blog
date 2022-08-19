from django.db import models
from datetime import datetime

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    fitness=models.CharField(max_length=100)
    coding=models.CharField(max_length=100)
    study=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    created_at=models.DateTimeField(default=datetime.now,blank=True)