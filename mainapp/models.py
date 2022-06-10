from django.db import models

# Create your models here.
class plan(models.Model):
    items=models.CharField(max_length=1000)
    