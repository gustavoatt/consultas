# -*- coding: utf-8 -*-
from django.contrib import messages
from django.forms.extras import widgets
from django.views.generic import DetailView, CreateView

from .forms import PacienteEditForm
from .models import Paciente

########## MIXINS
class FormActionMixin(object):
  """
  Adds a message to a view defined in the action variable that can be shown with
  django.contrib.messages.
  """
  @property
  def action(self):
    msg = "{} is missing action.".format(self.__class__)
    raise NotImplementedError(msg)

  def form_valid(self, form):
    messages.info(self.request, self.action)
    return super(FormActionMixin, self).form_valid(form)
########## END MIXINS

########## VIEWS
class PacienteCreateView(FormActionMixin, CreateView):
  model = Paciente
  action = "Paciente creado exitosamente."
  form_class = PacienteEditForm

class PacienteDetailView(DetailView):
  model = Paciente
  context_object_name = "paciente"
########## END VIEWS