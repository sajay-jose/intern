from django.db import models

# Create your models here.

class Register(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=60)
