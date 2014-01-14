import datetime

from django.core.exceptions import ValidationError

def validate_older_date(fecha):
  """Valida que la fecha suministrada sea menor que la fecha actual."""
  if fecha > datetime.date.today():
    msg = u'La fecha de nacimiento tiene que ser en el pasado o presente.'
    raise ValidationError(msg)