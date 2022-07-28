from pickle import TRUE
from django.db import models

# Create your models here.
class familia(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    nacimiento = models.DateField(auto_now_add=True)