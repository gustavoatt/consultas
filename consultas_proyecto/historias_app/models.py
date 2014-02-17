# -*- coding: utf-8 -*-
from django.db import models

from pacientes_app.models import Paciente

class Historia(models.Model):
  """Historia médica realizada a un paciente durante una visita."""
  paciente                 = models.ForeignKey(Paciente)
  fecha                    = models.DateTimeField(auto_now=True)
  motivo_consulta          = models.TextField(
                                 verbose_name=u'Motivo de Consulta'
                             )
  antecedentes_personales  = models.TextField(blank=True)
  antecedentes_familiares  = models.TextField(blank=True)
  habitos_psicobiologicos  = models.TextField(blank=True)
  examen_general           = models.TextField(blank=True)
  examen_piel              = models.TextField(blank=True)
  examen_cabeza            = models.TextField(blank=True)
  examen_ojos              = models.TextField(blank=True)
  examen_oidos             = models.TextField(blank=True)
  examen_nariz             = models.TextField(blank=True)
  examen_boca              = models.TextField(blank=True)
  examen_garganta          = models.TextField(blank=True)
  examen_respiratorio      = models.TextField(blank=True)
  examen_osteomuscular     = models.TextField(blank=True)
  examen_cardiovascular    = models.TextField(blank=True)
  examen_gastrointestinal  = models.TextField(blank=True)
  examen_genitourinario    = models.TextField(blank=True)
  examen_ginecologico      = models.TextField(blank=True)
  examen_nervioso_y_mental = models.TextField(blank=True)
  examen_epidemiologico    = models.TextField(blank=True)
  temperatura              = models.DecimalField(
                               max_digits=5, decimal_places=2, blank=True,
                               null=True
                             )
  pulso                    = models.DecimalField(
                               max_digits=5, decimal_places=2, blank=True,
                               null=True
                             )
  respiracion              = models.DecimalField(
                               max_digits=5, decimal_places=2, blank=True,
                               null=True
                             )
  tension_art_sist         = models.IntegerField(
                               blank=True, null=True,
                               verbose_name=u'Tensión Arterial Sistólica'
                             )
  tension_art_diast        = models.IntegerField(
                               blank=True, null=True,
                               verbose_name=u'Tensión Arterial Diástolica'
                             )
  frecuencia_cardiaca      = models.DecimalField(
                               max_digits=5, decimal_places=2, blank=True,
                               null=True
                             )
  peso                     = models.DecimalField(
                               max_digits=5, decimal_places=2, blank=True,
                               null=True,
                               help_text=u'Peso en Kilogramos'
                             )
  talla                    = models.DecimalField(
                               max_digits=7, decimal_places=2, blank=True,
                               null=True
                             )
  grasa_corporal           = models.DecimalField(
                               max_digits=7, decimal_places=2, blank=True,
                               null=True,
                               verbose_name=u'Índice de Masa Corporal'
                             )

  def get_examenes_fields(self):
    return [(field.verbose_name, field.value_to_string(self))
            for field in Historia._meta.fields
            if 'examen' in field.name]

  def get_signos_vitales_fields(self):
    signos_vitales_field_names = [
        'temperatura',
        'pulso',
        'respiracion',
        'tension_art_sist',
        'tension_art_diast',
        'frecuencia_cardiaca',
        'peso',
        'talla',
        'grasa_corporal'
    ]

    return [(field.verbose_name, field.value_to_string(self))
            for field in Historia._meta.fields
            if field.name in signos_vitales_field_names]


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
