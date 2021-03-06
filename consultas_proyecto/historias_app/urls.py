# -*- coding: utf-8 -*-
from django.conf import urls
from django.contrib.auth import decorators

from .views import HistoriaCreateView
from .views import HistoriaDetailView
from .views import HistoriaPacienteListView
from .views import HistoriaUpdateView

HISTORIA_CREATE_URL_NAME = 'historia_create'
HISTORIA_UPDATE_URL_NAME = 'historia_update'
HISTORIA_DETAIL_URL_NAME = 'historia_detail'
HISTORIA_LIST_URL_NAME   = 'historia_list'

urlpatterns = urls.patterns("",
    urls.url(
        regex=r'^nueva/$',
        view=decorators.login_required(HistoriaCreateView.as_view()),
        name=HISTORIA_CREATE_URL_NAME
    ),
    urls.url(
        regex=r'^editar/(?P<pk>\d+)$',
        view=decorators.login_required(HistoriaUpdateView.as_view()),
        name=HISTORIA_UPDATE_URL_NAME
    ),
    urls.url(
        regex=r'^(?P<pk>\d+)/$',
        view=decorators.login_required(HistoriaDetailView.as_view()),
        name=HISTORIA_DETAIL_URL_NAME
    ),
    urls.url(
        regex=r'^paciente/(?P<paciente_id>\d+)/$',
        view=decorators.login_required(HistoriaPacienteListView.as_view()),
        name=HISTORIA_LIST_URL_NAME
    )
)
