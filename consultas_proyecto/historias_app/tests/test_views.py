# -*- coding: utf-8 -*-
from django import test
from django.test import client
from django.core import urlresolvers

from pacientes_app import models as paciente_models

from historias_app import forms
from historias_app import models as historia_models
from historias_app import urls as historia_urls

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
        motivo_consulta='Prueba de consulta',
        examen_general='Todo en orden',
        temperatura=26,
        pulso=15.10
    )
    self.client = client.Client()

  def test_historia_create_view(self):
    response = self.client.get(urlresolvers.reverse(
        historia_urls.HISTORIA_CREATE_URL_NAME))
    self.assertEqual(200, response.status_code)
    self.assertIn('form', response.context)
    self.assertEqual(forms.HistoriaEditForm, response.context['form'].__class__)

    self.assertIn('Paciente', response.content)
    self.assertIn('Motivo de Consulta', response.content)

  def test_historia_update_view(self):
    """Tests that historia update view renders correctly."""
    response = self.client.get(urlresolvers.reverse(
        historia_urls.HISTORIA_UPDATE_URL_NAME,
        kwargs={'pk': self.historia.pk}))
    self.assertEqual(200, response.status_code)
    self.assertIn('form', response.context)
    self.assertEqual(forms.HistoriaEditForm, response.context['form'].__class__)

    self.assertIn('Paciente', response.content)
    self.assertIn('Motivo de Consulta', response.content)

  def test_historia_detail_view(self):
    response = self.client.get(urlresolvers.reverse(
        historia_urls.HISTORIA_DETAIL_URL_NAME,
        kwargs={'pk': self.historia.pk}
      )
    )
    self.assertEqual(200, response.status_code)
    self.assertIn('historia', response.context)

    self.assertIn('Gustavo', response.content)
    self.assertIn('Prueba de consulta', response.content)

    self.assertIn('Todo en orden', response.content)
    self.assertIn('26', response.content)
