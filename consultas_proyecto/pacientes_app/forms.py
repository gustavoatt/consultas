# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from crispy_forms import helper as crispy_helper
from crispy_forms import layout
from crispy_forms import bootstrap
import floppyforms

from .models import Paciente

class PacienteEditForm(LoginRequiredMixin, floppyforms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(PacienteEditForm, self).__init__(*args, **kwargs)

    self.helper = crispy_helper.FormHelper()
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-md-2'
    self.helper.field_class = 'col-md-4'
    self.helper.layout = layout.Layout(
        'cedula',
        'nombres',
        'apellidos',
        'fecha_nacimiento',
        'genero',
        'direccion',
        'ciudad',
        'estado',
        'telefono_casa',
        'telefono_celular',
        layout.HTML('<hr>'),
        bootstrap.FormActions(
            layout.Submit('submit', 'Agregar',
                css_class='col-md-offset-2 btn-default btn-success')
        )
    )


  class Meta:
    model = Paciente
    widgets = {
      'fecha_nacimiento': floppyforms.SelectDateWidget(
        years=xrange(1900, 2014)
      ),
    }