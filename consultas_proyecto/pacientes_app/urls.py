# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import PacienteDetailView, PacienteCreateView

urlpatterns = patterns("",
  url(
    regex=r'(?P<pk>\d+)/$',
    view=PacienteDetailView.as_view(),
    name='paciente_detail'
  ),
  url(
    regex=r'nuevo/$',
    view=PacienteCreateView.as_view(),
    name='paciente_create'
  ),
)