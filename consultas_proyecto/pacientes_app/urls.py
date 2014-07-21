# -*- coding: utf-8 -*-
from django.conf import urls

from .views import PacienteDetailView
from .views import PacienteCreateView
from .views import PacienteListView
from .views import PacienteUpdateView
from .views import PacienteSearchAPIView

PACIENTE_DETAIL_URL_NAME = 'paciente_detail'
PACIENTE_LIST_URL_NAME = 'paciente_list'
PACIENTE_CREATE_URL_NAME = 'paciente_create'
PACIENTE_SEARCH_API_URL_NAME = 'api_paciente_list'
PACIENTE_UPDATE_URL_NAME = 'paciente_update'

urlpatterns = urls.patterns("",
  urls.url(
    regex=r'^(?P<pk>\d+)/$',
    view=PacienteDetailView.as_view(),
    name=PACIENTE_DETAIL_URL_NAME
  ),
  urls.url(
    regex=r'^lista/$',
    view=PacienteListView.as_view(),
    name=PACIENTE_LIST_URL_NAME
  ),
  urls.url(
    regex=r'^nuevo/$',
    view=PacienteCreateView.as_view(),
    name=PACIENTE_CREATE_URL_NAME
  ),
  urls.url(
    regex=r'^editar/(?P<pk>\d+)/$',
    view=PacienteUpdateView.as_view(),
    name=PACIENTE_UPDATE_URL_NAME
  ),

  # API URLS
  urls.url(
    regex=r'^api/listar/$',
    view=PacienteSearchAPIView.as_view(),
    name=PACIENTE_SEARCH_API_URL_NAME
  )
)
