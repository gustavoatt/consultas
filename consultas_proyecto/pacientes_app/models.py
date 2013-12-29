# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

class Paciente(models.Model):
  """ Información básica necesaria de cualquier paciente. """
  # Constantes
  ESTADOS = (
    ('01', 'Amazonas'),
    ('02', 'Anzoátegui'),
    ('03', 'Apure'),
    ('04', 'Aragua'),
    ('05', 'Barinas'),
    ('06', 'Bolívar'),
    ('07', 'Carabobo'),
    ('08', 'Cojedes'),
    ('09', 'Delta Amacuro'),
    ('10', 'Distrito Capital'),
    ('11', 'Falcón'),
    ('12', 'Guárico'),
    ('13', 'Lara'),
    ('14', 'Los Roques'),
    ('15', 'Mérida'),
    ('16', 'Miranda'),
    ('17', 'Monagas'),
    ('18', 'Nueva Esparta'),
    ('19', 'Portuguesa'),
    ('20', 'Sucre'),
    ('21', 'Táchira'),
    ('22', 'Trujillo'),
    ('23', 'Vargas'),
    ('24', 'Yaracuy'),
    ('25', 'Zulia')
  )

  # Campos de un paciente
  cedula           = models.CharField(max_length=10, unique=True)
  nombres          = models.CharField(max_length=200)
  apellidos        = models.CharField(max_length=200)
  fecha_nacimiento = models.DateField()
  direccion        = models.TextField(blank=True)
  ciudad           = models.CharField(max_length=200)
  estado           = models.CharField(max_length=2, choices=ESTADOS)
  telefono_casa    = models.CharField(max_length=20, blank=True)
  telefono_celular = models.CharField(max_length=20, blank=True)

  class Meta:
    verbose_name = u'Paciente'
    verbose_name_plural = u'Pacientes'

  def __unicode__(self):
    return u'{} {} C.I.: {}'.format(self.nombres, self.apellidos, self.cedula)

  def get_absolute_url(self):
    return reverse('paciente_detail', kwargs={'pk': self.pk})