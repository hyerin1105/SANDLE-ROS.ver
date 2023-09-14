from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    ordering = '-pk'
    template_name = 'goods.html'

    def __str__(self):
        return f'{self.pk}, {self.username}'

    def get_absolute_url(self):
        return f'/goods/{self.pk}/'