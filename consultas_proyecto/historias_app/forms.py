# -*- coding: utf-8 -*-
from crispy_forms import helper as crispy_helper
from crispy_forms import layout
from crispy_forms import bootstrap
import floppyforms

from .models import Historia

class HistoriaEditForm(floppyforms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(HistoriaEditForm, self).__init__(*args, **kwargs)

    self.helper = crispy_helper.FormHelper()
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-md-2'
    self.helper.field_class = 'col-md-4'
    self.helper.help_text_inline = True
    self.helper.layout = layout.Layout(
        bootstrap.TabHolder(
            bootstrap.Tab(u'Información Básica',
                'paciente',
                'motivo_consulta',
                'antecedentes_personales',
                'antecedentes_familiares',
                'habitos_psicobiologicos'
            ),
            bootstrap.Tab(u'Exámenes',
                'examen_general',
                'examen_piel',
                'examen_cabeza',
                'examen_ojos',
                'examen_nariz',
                'examen_boca',
                'examen_garganta',
                'examen_respiratorio',
                'examen_osteomuscular',
                'examen_cardiovascular',
                'examen_gastrointestinal',
                'examen_genitourinario',
                'examen_ginecologico',
                'examen_nervioso_y_mental',
                'examen_epidemiologico'
            ),
            bootstrap.Tab(u'Signos vitales',
                'temperatura',
                'pulso',
                'respiracion',
                'tension_art_sist',
                'tension_art_diast',
                'frecuencia_cardiaca',
                'peso',
                'talla',
                'grasa_corporal'
            )
        ),
        layout.HTML('<hr>'),
        bootstrap.FormActions(
            layout.Submit(
                'submit', 'Agregar',
                css_class='col-md-offset-2 btn-default btn-success'
            )
        )
    )

  class Meta:
    model = Historia