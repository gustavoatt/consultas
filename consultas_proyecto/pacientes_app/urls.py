# -*- coding: utf-8 -*-
from django.conf import urls
from django.contrib.auth import decorators
from django.contrib.auth import views as auth_views
from django.conf import settings

from .views import PacienteDetailView
from .views import PacienteCreateView
from .views import PacienteListView
from .views import PacienteUpdateView
from .views import PacienteSearchAPIView

LOGIN_URL_NAME = 'login'

# URL Names.
PACIENTE_DETAIL_URL_NAME     = 'paciente_detail'
PACIENTE_LIST_URL_NAME       = 'paciente_list'
PACIENTE_CREATE_URL_NAME     = 'paciente_create'
PACIENTE_SEARCH_API_URL_NAME = 'api_paciente_list'
PACIENTE_UPDATE_URL_NAME     = 'paciente_update'

settings.LOGIN_URL = LOGIN_URL_NAME

urlpatterns = urls.patterns("",
  # Global urls
  urls.url(
      regex=r'^autenticar/$',
      view=auth_views.login,
      name=LOGIN_URL_NAME
  ),

  # Pacientes urls
  urls.url(
      regex=r'^(?P<pk>\d+)/$',
      view=decorators.login_required(PacienteDetailView.as_view()),
      name=PACIENTE_DETAIL_URL_NAME
  ),
  urls.url(
      regex=r'^lista/$',
      view=decorators.login_required(PacienteListView.as_view()),
      name=PACIENTE_LIST_URL_NAME
  ),
  urls.url(
      regex=r'^nuevo/$',
      view=decorators.login_required(PacienteCreateView.as_view()),
      name=PACIENTE_CREATE_URL_NAME
  ),
  urls.url(
      regex=r'^editar/(?P<pk>\d+)/$',
      view=decorators.login_required(PacienteUpdateView.as_view()),
      name=PACIENTE_UPDATE_URL_NAME
  ),

  # API URLS
  urls.url(
    regex=r'^api/listar/$',
    view=decorators.login_required(PacienteSearchAPIView.as_view()),
    name=PACIENTE_SEARCH_API_URL_NAME
  )
)
