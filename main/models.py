from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    address = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.address