# -*- coding: utf-8 -*-
from django.views.generic import DetailView, CreateView
from django.forms.extras import widgets

from .models import Paciente
from .forms import PacienteEditForm

class PacienteCreateView(CreateView):
  model = Paciente
  form_class = PacienteEditForm

class PacienteDetailView(DetailView):
  model = Paciente
  context_object_name = 'paciente'
