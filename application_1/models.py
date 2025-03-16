from django.db import models
# Create your models here.


class Database(models.Model):
    x = models.CharField(max_length=1000)
    y = models.CharField(max_length=1000)