# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil import relativedelta

from django.core import urlresolvers
from django.core.exceptions import ValidationError
from django.db import models

from .validators import validate_older_date

class Paciente(models.Model):
  """ Información básica necesaria de cualquier paciente. """
  # Constantes
  ESTADOS = (
    (u'01', u'Amazonas'),
    (u'02', u'Anzoátegui'),
    (u'03', u'Apure'),
    (u'04', u'Aragua'),
    (u'05', u'Barinas'),
    (u'06', u'Bolívar'),
    (u'07', u'Carabobo'),
    (u'08', u'Cojedes'),
    (u'09', u'Delta Amacuro'),
    (u'10', u'Distrito Capital'),
    (u'11', u'Falcón'),
    (u'12', u'Guárico'),
    (u'13', u'Lara'),
    (u'14', u'Los Roques'),
    (u'15', u'Mérida'),
    (u'16', u'Miranda'),
    (u'17', u'Monagas'),
    (u'18', u'Nueva Esparta'),
    (u'19', u'Portuguesa'),
    (u'20', u'Sucre'),
    (u'21', u'Táchira'),
    (u'22', u'Trujillo'),
    (u'23', u'Vargas'),
    (u'24', u'Yaracuy'),
    (u'25', u'Zulia'),
    (u'26', u'Exterior')
  )
  GENEROS = (
    (u'01', u'Femenino'),
    (u'02', u'Masculino')
  )

  # Campos de un paciente
  cedula           = models.CharField(max_length=10, unique=True)
  nombres          = models.CharField(max_length=200)
  apellidos        = models.CharField(max_length=200)
  fecha_nacimiento = models.DateField(validators=[validate_older_date])
  genero           = models.CharField(max_length=2, choices=GENEROS)
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
    return urlresolvers.reverse('paciente_detail', kwargs={'pk': self.pk})

  def edad(self, fecha=None):
    """ Regresa la edad de este paciente a la hora de ser llamado.

    Args:
      fecha: la fecha desde la cual se contará la edad. Por defecto se usará la
        fecha de hoy. La fecha de hoy debe ser un datetime para mayor precisión.
    """
    if fecha is None:
      fecha = datetime.today()

    if self.fecha_nacimiento > fecha.date():
      msg = u'La fecha de nacimiento es en el futuro.'
      raise ValidationError(msg)

    delta = relativedelta.relativedelta(fecha, self.fecha_nacimiento)
    return delta.years
