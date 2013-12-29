import floppyforms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from braces.views import LoginRequiredMixin

from .models import Paciente

class PacienteEditForm(LoginRequiredMixin, floppyforms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(PacienteEditForm, self).__init__(*args, **kwargs)

    self.helper = FormHelper()
    self.helper.form_tag = False

  class Meta:
    model = Paciente
    widgets = {
      'fecha_nacimiento': floppyforms.DateInput(),
    }