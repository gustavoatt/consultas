# -*- coding: utf-8 -*-
from django.views.generic import DetailView, CreateView
from django.forms.extras import widgets

from .models import Paciente

class PacienteCreateView(CreateView):
  model = Paciente

class PacienteDetailView(DetailView):
  model = Paciente
  context_object_name = 'paciente'
