from django.test import TestCase

from pacientes_app.forms import PacienteEditForm
from pacientes_app.models import Paciente

class PacienteEditFormTestCase(TestCase):
  def setUp(self):
    self.pacient = Paciente.objects.create(
        cedula='18423347',
        fecha_nacimiento='1988-03-26'
    )

  def test_valid_form(self):
    data = {'cedula': '19883999',
            'nombres': 'Naymar',
            'apellidos': 'Torres',
            'fecha_nacimiento': '1989-10-12',
            'estado': Paciente.ESTADOS[0][0],
            'ciudad': 'Puerto Ayacucho',
    }
    form = PacienteEditForm(data=data)
    self.assertTrue(form.is_valid())

  def test_invalid_form(self):
    data = {'cedula': '18423347',
            'nombres': 'Pepe',
            'apellidos': 'Aguilar',
            'fecha_nacimiento': '2014-01-01'
    }
    form = PacienteEditForm(data=data)
    self.assertFalse(form.is_valid())
