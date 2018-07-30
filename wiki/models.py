from django.db import models

# Create your models here.
class character(models.Model):
    full_name = models.CharField(max_length=50)
    aliases = models.TextField()
    age  = models.SmallIntegerField()
    height = models.CharField(max_length=6)
    origin = models.CharField(max_length=40)
    affiliations = models.TextField()
    relationships = models.TextField()
