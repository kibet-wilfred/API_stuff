from django.db import models
from django import forms

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=10)


