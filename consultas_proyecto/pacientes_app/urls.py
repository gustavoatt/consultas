# -*- coding: utf-8 -*-
from django.conf import urls

from .views import PacienteDetailView
from .views import PacienteCreateView
from .views import PacienteListView
from .views import PacienteUpdateView

urlpatterns = urls.patterns("",
  urls.url(
    regex=r'^(?P<pk>\d+)/$',
    view=PacienteDetailView.as_view(),
    name='paciente_detail'
  ),
  urls.url(
    regex=r'^lista/$',
    view=PacienteListView.as_view(),
    name='paciente_list'
  ),
  urls.url(
    regex=r'^nuevo/$',
    view=PacienteCreateView.as_view(),
    name='paciente_create'
  ),
  urls.url(
    regex=r'^editar/(?P<pk>\d+)/$',
    view=PacienteUpdateView.as_view(),
    name='paciente_update'
  )
)
