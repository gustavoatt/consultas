# -*- coding: utf-8 -*-
from django.db import models

from pacientes_app.models import Paciente

class Historia(models.Model):
  paciente = models.ForeignKey(Paciente)

class Examen(models.Model):
  fecha_creacion = models.DateTimeField(auto_now=True)

class ResultadoExamen(models.Model):
  TIPO_DATOS_CHOICE = (
      (u'01', u'Númerico'),
      (u'02', u'Texto'),
      (u'03', u'Sí o No')
  )

  nombre = models.CharField(max_length=200)
  tipo_dato = models.CharField(max_length=10, choices=TIPO_DATOS_CHOICE)
  unidad = models.CharField(max_length=20)
  valor  = models.CharField(max_length=400)
