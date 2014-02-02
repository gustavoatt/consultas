# -*- coding: utf-8 -*-
from django import test
from django.test import client
from django.core import urlresolvers

from pacientes_app import models as paciente_models

from historias_app import models as historia_models
from historias_app import forms

HISTORIA_CREATE_URL_NAME = 'historia_create'
HISTORIA_DETAIL_URL_NAME = 'historia_detail'

class HistoriasAppViewTest(test.TestCase):
  def setUp(self):
    self.paciente = paciente_models.Paciente.objects.create(
        cedula='18423347',
        nombres='Gustavo Adolfo',
        apellidos='Torres Torres',
        fecha_nacimiento='1988-03-26'
    )
    self.historia = historia_models.Historia.objects.create(
        paciente=self.paciente,
        motivo_consulta='Prueba de consulta'
    )
    self.client = client.Client()

  def test_historia_create_view(self):
    response = self.client.get(urlresolvers.reverse(HISTORIA_CREATE_URL_NAME))
    self.assertEqual(200, response.status_code)
    self.assertTrue('form' in response.context)
    self.assertEqual(forms.HistoriaEditForm, response.context['form'].__class__)

    self.assertTrue('Paciente' in response.content)
    self.assertTrue('Motivo de Consulta' in response.content)

  def test_historia_detail_view(self):
    response = self.client.get(urlresolvers.reverse(
        HISTORIA_DETAIL_URL_NAME,
        kwargs={'pk': self.historia.pk}
      )
    )
    self.assertEqual(200, response.status_code)
    self.assertTrue('historia' in response.context)

    self.assertTrue('Gustavo' in response.content)
    self.assertTrue('Prueba de consulta' in response.content)