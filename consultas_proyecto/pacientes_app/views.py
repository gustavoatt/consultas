# -*- coding: utf-8 -*-
from django.contrib import messages
from django.db.models import Q
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
  """Shows all the patients in a list matching a certaing query.

  GET Args:
    q: query that will be used to search on the patients.
  """
  model = Paciente
  context_object_name = "pacientes"
  paginate_by = 10

  def get_queryset(self):
    """Return all Paciente objects is no query is passed, otherwise search for
    the matching Paciente objects via the q parameter."""
    query = self.request.GET.get('q', None)

    if query:
      words = query.split()
      lookups = [Q(cedula__icontains=word) | Q(nombres__icontains=word) |
                 Q(apellidos__icontains=word) for word in words]
      return Paciente.objects.filter(*lookups)
    else:
      return super(PacienteListView, self).get_queryset()

class PacienteSearchAPIView(rest_generic.ListAPIView):
  """Looks up patient information and returns it serialized. Good for AJAX."""
  class CustomSearchFilter(rest_filters.SearchFilter):
    search_param = 'q'

  model = Paciente
  queryset = Paciente.objects.all()
  serializer_class = PacienteSerializer
  filter_backends = (CustomSearchFilter,)
  search_fields = ('cedula', 'nombres', 'apellidos')
########## END VIEWS
