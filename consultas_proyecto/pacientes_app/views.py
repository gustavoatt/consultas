# -*- coding: utf-8 -*-
from django.contrib import messages
from django.forms.extras import widgets
from django.views import generic

from rest_framework import generics as rest_generic
from rest_framework import filters as rest_filters

from .forms import PacienteEditForm
from .models import Paciente
from .serializers import PacienteSerializer

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

class PacienteSearchAPIView(rest_generic.ListAPIView):
  class CustomSearchFilter(rest_filters.SearchFilter):
    search_param = 'q'

  model = Paciente
  queryset = Paciente.objects.all()
  serializer_class = PacienteSerializer
  filter_backends = (CustomSearchFilter,)
  search_fields = ('cedula', 'nombres', 'apellidos')
########## END VIEWS
