from django.db import models
from trainer.models import trainer

# Create your models here.

class intern(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_approved = models.BooleanField(default=False)
    assigned_trainer = models.ForeignKey(trainer, on_delete=models.SET_NULL, null=True, blank=True)

class internregister(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    Linkedin_Link = models.URLField(blank=True)
    Github_Link = models.URLField(blank=True)
    Skills = models.CharField(max_length=300)
    password = models.CharField(max_length=50, blank=False)


