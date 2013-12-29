# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paciente'
        db.create_table(u'pacientes_app_paciente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'pacientes_app', ['Paciente'])


    def backwards(self, orm):
        # Deleting model 'Paciente'
        db.delete_table(u'pacientes_app_paciente')


    models = {
        u'pacientes_app.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['pacientes_app']