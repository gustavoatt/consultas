import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from pacientes_app.models import Paciente

class PacienteTest(TestCase):
  def setUp(self):
    self.paciente = Paciente.objects.create(
      cedula='18423347',
      fecha_nacimiento='1988-03-26'
    )
    self.paciente.save()
    self.paciente = Paciente.objects.get(cedula='18423347')

  def test_edad(self):
    self.assertEquals(25, self.paciente.edad(
        fecha=datetime.datetime.strptime('2013-03-26', '%Y-%m-%d')))
    self.assertEquals(24, self.paciente.edad(
        fecha=datetime.datetime.strptime('2013-03-25', '%Y-%m-%d')))

    self.assertRaises(ValidationError, self.paciente.edad,
                      datetime.datetime.strptime('1987-02-26', '%Y-%m-%d'))
    # TODO(gustavoatt) Probar con diferentes husos horarios


