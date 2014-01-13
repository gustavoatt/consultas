from braces.views import LoginRequiredMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms

from .models import Paciente

class PacienteEditForm(LoginRequiredMixin, floppyforms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(PacienteEditForm, self).__init__(*args, **kwargs)

    self.helper = FormHelper()
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-md-2'
    self.helper.field_class = 'col-md-4'
    self.helper.add_input(
      Submit('submit', 'Agregar', css_class='col-md-offset-2')
    )

  class Meta:
    model = Paciente
    widgets = {
      'fecha_nacimiento': floppyforms.DateInput(),
    }