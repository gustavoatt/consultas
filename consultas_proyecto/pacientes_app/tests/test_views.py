# -*- coding: utf-8 -*-
from django import test
from django.test import client
from django.core import urlresolvers

from pacientes_app import models
from pacientes_app import views
from pacientes_app import forms

PACIENTE_DETAIL_URL_NAME = 'paciente_detail'
PACIENTE_LIST_URL_NAME = 'paciente_list'
PACIENTE_CREATE_URL_NAME = 'paciente_create'

class PacientesAppViewsTest(test.TestCase):
  def setUp(self):
    self.paciente = models.Paciente.objects.create(
        cedula='18423347',
        nombres='Gustavo Adolfo',
        apellidos='Torres Torres',
        fecha_nacimiento='1988-03-26'
    )
    self.client = client.Client()

  def test_paciente_detail_view(self):
    response = self.client.get(urlresolvers.reverse(
        PACIENTE_DETAIL_URL_NAME,
        kwargs={'pk': self.paciente.pk}
      )
    )
    self.assertEqual(200, response.status_code)
    self.assertTrue('paciente' in response.context)

    self.assertTrue('Gustavo' in response.content)
    self.assertTrue('Torres' in response.content)

  def test_paciente_create_view(self):
    response = self.client.get(urlresolvers.reverse(PACIENTE_CREATE_URL_NAME))
    self.assertEqual(200, response.status_code)
    self.assertTrue('form' in response.context)
    self.assertEqual(forms.PacienteEditForm, response.context['form'].__class__)

    self.assertTrue('Nombres' in response.content)
    self.assertTrue('Apellidos' in response.content)

  def test_paciente_list_view(self):
    models.Paciente.objects.create(
        cedula='13785815',
        nombres='Ithamar Alexander',
        fecha_nacimiento='1980-04-20'
    )
    response = self.client.get(urlresolvers.reverse(PACIENTE_LIST_URL_NAME))
    self.assertEqual(200, response.status_code)
    self.assertTrue('pacientes' in response.context)

    self.assertTrue('Ithamar' in response.content)
    self.assertTrue('Gustavo' in response.content)