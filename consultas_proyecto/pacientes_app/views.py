# -*- coding: utf-8 -*-
from django.contrib import messages
from django.forms.extras import widgets
from django.views import generic

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
class PacienteCreateView(FormActionMixin, generic.CreateView):
  model = Paciente
  action = "Paciente creado exitosamente."
  form_class = PacienteEditForm

class PacienteUpdateView(generic.UpdateView):
  model = Paciente
  form_class = PacienteEditForm

class PacienteDetailView(generic.DetailView):
  model = Paciente
  context_object_name = "paciente"

class PacienteListView(generic.list.ListView):
  model = Paciente
  context_object_name = "pacientes"
  paginate_by = 10
########## END VIEWS
