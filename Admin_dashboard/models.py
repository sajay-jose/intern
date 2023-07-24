from django.db import models

# Create your models here.
class admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class trainerregister(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=200)
    password = models.CharField(max_length=50, blank=False)