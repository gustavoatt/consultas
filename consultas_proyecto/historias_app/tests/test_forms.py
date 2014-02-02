# -*- coding: utf-8 -*-
from django import test

from historias_app import forms
from historias_app import models as historias_models
from pacientes_app import models as pacientes_models

class HistoriaEditFormTestCase(test.TestCase):
  def setUp(self):
    self.paciente = pacientes_models.Paciente.objects.create(
        cedula='18423347',
        fecha_nacimiento='1988-03-26'
    )

  def test_valid_form(self):
    data = {
      'paciente': self.paciente.pk,
      'motivo_consulta': u'Probar que la aplicación funcione',
      'examen_piel': u'Todo en orden'
    }
    form = forms.HistoriaEditForm(data=data)
    self.assertTrue(form.is_valid(), form.errors)

    form.save()
    self.assertEquals(1, historias_models.Historia.objects.count())

  def test_invalid_form_missing_motivo_consulta(self):
    data = {
      'paciente': self.paciente.pk,
      'examen_piel': u'Todo en orden'
    }
    form = forms.HistoriaEditForm(data=data)
    self.assertFalse(form.is_valid())
    self.assertTrue('motivo_consulta' in form.errors)