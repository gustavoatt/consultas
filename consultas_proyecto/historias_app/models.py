# -*- coding: utf-8 -*-
from django.db import models

from pacientes_app.models import Paciente

class Historia(models.Model):
  paciente = models.ForeignKey(Paciente)
  fecha = models.DateTimeField(auto_now=True)
  motivo_consulta = models.TextField()

class Examen(models.Model):
  historia = models.ForeignKey(Historia)
  fecha_creacion = models.DateTimeField(auto_now_add=True)

class TipoResultadoExamen(models.Model):
  TIPO_DATOS_CHOICE = (
      (u'01', u'Númerico'),
      (u'02', u'Texto'),
      (u'03', u'Sí o No')
  )

  nombre = models.CharField(max_length=200)
  tipo_dato = models.CharField(max_length=2, choices=TIPO_DATOS_CHOICE)
  unidad = models.CharField(max_length=50)

  class Meta:
    ordering = ['nombre']

class ResultadoExamen(models.Model):
  examen = models.ForeignKey(Examen)
  tipo_resultado_examen = models.ForeignKey(TipoResultadoExamen)
  valor  = models.CharField(max_length=400)
  fecha  = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['fecha']
