from django.db import models

# Create your models here.

class Player(models.Model):

    nombre          = models.CharField(max_length=32)
    nivel           = models.CharField(max_length=8)
    goles           = models.IntegerField()
    sueldo          = models.FloatField()
    bono            = models.FloatField()
    sueldo_completo = models.FloatField(null=True, blank=True)
    equipo          = models.CharField(max_length=15)