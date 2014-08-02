# -*- coding: utf-8 -*-
from django import test
from django.contrib.auth import models as auth_models
from django.core import urlresolvers
from django.test import client

from rest_framework.test import APIClient

from pacientes_app import models
from pacientes_app import views
from pacientes_app import forms
from pacientes_app import serializers
from pacientes_app import urls as paciente_urls

class PacientesAppViewsTest(test.TestCase):
  LOGGED_USERNAME = 'test_user'
  LOGGED_PASSWORD = 'secret'

  def setUp(self):
    self.user = auth_models.User.objects.create_user(
        username=self.LOGGED_USERNAME, password=self.LOGGED_PASSWORD)
    self.paciente = models.Paciente.objects.create(
        cedula='18423347',
        nombres='Gustavo Adolfo',
        apellidos='Torres Torres',
        fecha_nacimiento='1988-03-26'
    )

    self.client = client.Client()
    self.assertTrue(self.client.login(username=self.LOGGED_USERNAME,
                                      password=self.LOGGED_PASSWORD))

  def test_paciente_detail_view(self):
    response = self.client.get(urlresolvers.reverse(
        paciente_urls.PACIENTE_DETAIL_URL_NAME,
        kwargs={'pk': self.paciente.pk}
      )
    )
    self.assertEqual(200, response.status_code)
    self.assertTrue('paciente' in response.context)

    self.assertTrue('Gustavo' in response.content)
    self.assertTrue('Torres' in response.content)

  def test_paciente_create_view(self):
    response = self.client.get(urlresolvers.reverse(
        paciente_urls.PACIENTE_CREATE_URL_NAME))
    self.assertEqual(200, response.status_code)
    self.assertTrue('form' in response.context)
    self.assertEqual(forms.PacienteEditForm, response.context['form'].__class__)

    self.assertTrue('Nombres' in response.content)
    self.assertTrue('Apellidos' in response.content)

  def test_paciente_list_view(self):
    models.Paciente.objects.create(
        cedula='13785815',
        nombres='Ithamar Alexander',
        apellidos='Torres',
        fecha_nacimiento='1980-04-20'
    )

    # When no query is passed, the view should list all patients in the database.
    response = self.client.get(urlresolvers.reverse(
        paciente_urls.PACIENTE_LIST_URL_NAME))
    self.assertEqual(200, response.status_code)
    self.assertTrue('pacientes' in response.context)

    self.assertIn('Ithamar', response.content)
    self.assertIn('Gustavo', response.content)

    # Search for a specific patient by cedula.
    response = self.client.get(urlresolvers.reverse(
        paciente_urls.PACIENTE_LIST_URL_NAME), {'q': '18423347'})

    self.assertIn('Gustavo', response.content)
    self.assertNotIn('Ithamar', response.content)

    # Search by name.
    response = self.client.get(urlresolvers.reverse(
        paciente_urls.PACIENTE_LIST_URL_NAME), {'q': 'Alexander'})

    self.assertIn('Alexander', response.content)
    self.assertNotIn('Gustavo', response.content)

    # Search by lastname.
    response = self.client.get(urlresolvers.reverse(
        paciente_urls.PACIENTE_LIST_URL_NAME), {'q': 'Tor'})

    self.assertIn('Ithamar', response.content)
    self.assertIn('Gustavo', response.content)

    # Search on multiple fields.
    response = self.client.get(urlresolvers.reverse(
        paciente_urls.PACIENTE_LIST_URL_NAME), {'q': 'Ithamar Torres'})

    self.assertIn('Ithamar', response.content)
    self.assertNotIn('Gustavo', response.content)

  def test_paciente_search_api_view(self):
    newer_pac = models.Paciente.objects.create(
        cedula='13785815',
        nombres='Ithamar Alexander',
        apellidos='Torres Torres',
        fecha_nacimiento='1980-04-20'
    )

    url = urlresolvers.reverse(paciente_urls.PACIENTE_SEARCH_API_URL_NAME)
    api_client = APIClient()
    self.assertTrue(api_client.login(username=self.LOGGED_USERNAME,
                                     password=self.LOGGED_PASSWORD))

    response = api_client.get(url, format='json')

    serialized_data1 = serializers.PacienteSerializer(self.paciente).data
    serialized_data2 = serializers.PacienteSerializer(newer_pac).data
    self.assertIn(serialized_data1, response.data)
    self.assertIn(serialized_data2, response.data)

    # Test filtered results
    response = api_client.get(url + '?q=gustavo', format='json')

    self.assertIn(serialized_data1, response.data)
    self.assertNotIn(serialized_data2, response.data)
