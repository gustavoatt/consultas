# -*- coding: utf-8 -*-
from django.conf import urls

from .views import HistoriaCreateView
from .views import HistoriaDetailView
from .views import HistoriaPacienteListView
from .views import HistoriaUpdateView

urlpatterns = urls.patterns("",
    urls.url(
        regex=r'^nueva/$',
        view=HistoriaCreateView.as_view(),
        name='historia_create'
    ),
    urls.url(
        regex=r'^editar/(?P<pk>\d+)$',
        view=HistoriaUpdateView.as_view(),
        name='historia_update'
    ),
    urls.url(
        regex=r'^(?P<pk>\d+)/$',
        view=HistoriaDetailView.as_view(),
        name='historia_detail'
    ),
    urls.url(
        regex=r'^paciente/(?P<paciente_id>\d+)/$',
        view=HistoriaPacienteListView.as_view(),
        name='historia_list'
    )
)
