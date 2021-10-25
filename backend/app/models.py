from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
