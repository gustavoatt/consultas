# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Paciente.ciudad'
        db.add_column(u'pacientes_app_paciente', 'ciudad',
                      self.gf('django.db.models.fields.CharField')(default='Barquisimeto', max_length=200),
                      keep_default=False)

        # Adding field 'Paciente.estado'
        db.add_column(u'pacientes_app_paciente', 'estado',
                      self.gf('django.db.models.fields.CharField')(default='13', max_length=2),
                      keep_default=False)


        # Changing field 'Paciente.nombres'
        db.alter_column(u'pacientes_app_paciente', 'nombres', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Paciente.apellidos'
        db.alter_column(u'pacientes_app_paciente', 'apellidos', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Deleting field 'Paciente.ciudad'
        db.delete_column(u'pacientes_app_paciente', 'ciudad')

        # Deleting field 'Paciente.estado'
        db.delete_column(u'pacientes_app_paciente', 'estado')


        # Changing field 'Paciente.nombres'
        db.alter_column(u'pacientes_app_paciente', 'nombres', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Paciente.apellidos'
        db.alter_column(u'pacientes_app_paciente', 'apellidos', self.gf('django.db.models.fields.CharField')(max_length=60))

    models = {
        u'pacientes_app.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'direccion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['pacientes_app']