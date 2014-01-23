# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Paciente.genero'
        db.add_column(u'pacientes_app_paciente', 'genero',
                      self.gf('django.db.models.fields.CharField')(default='02', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Paciente.genero'
        db.delete_column(u'pacientes_app_paciente', 'genero')


    models = {
        u'pacientes_app.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'direccion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['pacientes_app']