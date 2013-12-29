# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Paciente.cedula'
        db.add_column(u'pacientes_app_paciente', 'cedula',
                      self.gf('django.db.models.fields.CharField')(default='No C.I.', unique=True, max_length=10),
                      keep_default=False)

        # Adding field 'Paciente.fecha_nacimiento'
        db.add_column(u'pacientes_app_paciente', 'fecha_nacimiento',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 28, 0, 0)),
                      keep_default=False)

        # Adding field 'Paciente.telefono_casa'
        db.add_column(u'pacientes_app_paciente', 'telefono_casa',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'Paciente.telefono_celular'
        db.add_column(u'pacientes_app_paciente', 'telefono_celular',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)


        # Changing field 'Paciente.direccion'
        db.alter_column(u'pacientes_app_paciente', 'direccion', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting field 'Paciente.cedula'
        db.delete_column(u'pacientes_app_paciente', 'cedula')

        # Deleting field 'Paciente.fecha_nacimiento'
        db.delete_column(u'pacientes_app_paciente', 'fecha_nacimiento')

        # Deleting field 'Paciente.telefono_casa'
        db.delete_column(u'pacientes_app_paciente', 'telefono_casa')

        # Deleting field 'Paciente.telefono_celular'
        db.delete_column(u'pacientes_app_paciente', 'telefono_celular')


        # Changing field 'Paciente.direccion'
        db.alter_column(u'pacientes_app_paciente', 'direccion', self.gf('django.db.models.fields.CharField')(max_length=250))

    models = {
        u'pacientes_app.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'direccion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['pacientes_app']