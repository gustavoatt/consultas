from django import test

from pacientes_app import forms
from pacientes_app import models

class PacienteEditFormTestCase(test.TestCase):
  def setUp(self):
    self.paciente = models.Paciente.objects.create(
        cedula='18423347',
        fecha_nacimiento='1988-03-26'
    )

  def test_valid_form(self):
    data = {'cedula': '19883999',
            'nombres': 'Naymar',
            'apellidos': 'Torres',
            'genero': models.Paciente.GENEROS[0][0],
            'fecha_nacimiento': '1989-10-12',
            'estado': models.Paciente.ESTADOS[0][0],
            'ciudad': 'Puerto Ayacucho',
    }
    form = forms.PacienteEditForm(data=data)
    self.assertTrue(form.is_valid(), form.errors)

    form.save()
    self.assertEquals(2, models.Paciente.objects.count())

  def test_invalid_form_unique_cedula(self):
    data = {'cedula': '18423347',
            'nombres': 'Pepe',
            'apellidos': 'Aguilar',
            'fecha_nacimiento': '2014-01-01',
            'genero': models.Paciente.GENEROS[0][0],
            'estado': models.Paciente.ESTADOS[0][0],
            'ciudad': 'La Paz',
    }
    form = forms.PacienteEditForm(data=data)
    self.assertFalse(form.is_valid())
    self.assertTrue('cedula' in form.errors)

  def test_invalid_form_missing_fields(self):
    data = {'cedula': '13875815',
        'nombres': 'Ithamar Alexander',
        'apellidos': 'Torres Torres'
    }
    form = forms.PacienteEditForm(data=data)
    self.assertFalse(form.is_valid())
    self.assertTrue('fecha_nacimiento' in form.errors)
