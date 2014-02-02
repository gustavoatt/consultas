# -*- coding: utf-8 -*-
from django.views import generic

from pacientes_app import models as paciente_models

from .forms import HistoriaEditForm
from .models import Historia

########## VIEWS
class HistoriaCreateView(generic.CreateView):
  model = Historia
  form_class = HistoriaEditForm

class HistoriaDetailView(generic.DetailView):
  model = Historia
  context_object_name = "historia"

class HistoriaPacienteListView(generic.list.ListView):
  model = Historia
  context_object_name = "historias"

  def get_queryset(self, *args, **kwargs):
    if 'paciente_id' in self.kwargs:
      self.paciente = paciente_models.Paciente.objects.get(
          id=self.kwargs['paciente_id'])
      return Historia.objects.filter(paciente=self.paciente)
    else:
      return super(HistoriaPacienteListView, self).get_queryset(*args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super(HistoriaPacienteListView, self).get_context_data(**kwargs)
    context['paciente'] = self.paciente
    return context
