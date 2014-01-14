import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from pacientes_app.validators import validate_older_date

class ValidatorTest(TestCase):
  def test_validate_older_date(self):
    self.assertRaises(
      ValidationError,
      validate_older_date,
      datetime.datetime.strptime('5000-03-26', '%Y-%m-%d').date()
    )
    validate_older_date(
      datetime.datetime.strptime('1988-03-26', '%Y-%m-%d').date())