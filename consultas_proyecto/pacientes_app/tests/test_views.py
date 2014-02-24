# -*- coding: utf-8 -*-
from django import test
from django.test import client
from django.core import urlresolvers

from rest_framework.test import APIClient

from pacientes_app import models
from pacientes_app import views
from pacientes_app import forms
from pacientes_app import serializers

PACIENTE_DETAIL_URL_NAME = 'paciente_detail'
PACIENTE_LIST_URL_NAME = 'paciente_list'
PACIENTE_CREATE_URL_NAME = 'paciente_create'
PACIENTE_SEARCH_API_URL_NAME = 'api_paciente_list'

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

  def test_paciente_search_api_view(self):
    newer_pac = models.Paciente.objects.create(
        cedula='13785815',
        nombres='Ithamar Alexander',
        apellidos='Torres Torres',
        fecha_nacimiento='1980-04-20'
    )

    url = urlresolvers.reverse(PACIENTE_SEARCH_API_URL_NAME)
    api_client = APIClient()

    response = api_client.get(url, format='json')

    serialized_data1 = serializers.PacienteSerializer(self.paciente).data
    serialized_data2 = serializers.PacienteSerializer(newer_pac).data
    self.assertTrue(serialized_data1 in response.data)
    self.assertTrue(serialized_data2 in response.data)

    # Test filtered results
    response = api_client.get(url + '?q=gustavo', format='json')

    self.assertTrue(serialized_data1 in response.data)
    self.assertFalse(serialized_data2 in response.data)
