from django.db import models

class Paciente(models.Model):
  nombres   = models.CharField(max_length=60)
  apellidos = models.CharField(max_length=60)
  direccion = models.CharField(max_length=250)
