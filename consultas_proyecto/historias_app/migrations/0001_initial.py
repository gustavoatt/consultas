# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Historia'
        db.create_table(u'historias_app_historia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pacientes_app.Paciente'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('motivo_consulta', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'historias_app', ['Historia'])

        # Adding model 'Examen'
        db.create_table(u'historias_app_examen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('historia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historias_app.Historia'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'historias_app', ['Examen'])

        # Adding model 'TipoResultadoExamen'
        db.create_table(u'historias_app_tiporesultadoexamen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipo_dato', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'historias_app', ['TipoResultadoExamen'])

        # Adding model 'ResultadoExamen'
        db.create_table(u'historias_app_resultadoexamen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('examen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historias_app.Examen'])),
            ('tipo_resultado_examen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['historias_app.TipoResultadoExamen'])),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'historias_app', ['ResultadoExamen'])


    def backwards(self, orm):
        # Deleting model 'Historia'
        db.delete_table(u'historias_app_historia')

        # Deleting model 'Examen'
        db.delete_table(u'historias_app_examen')

        # Deleting model 'TipoResultadoExamen'
        db.delete_table(u'historias_app_tiporesultadoexamen')

        # Deleting model 'ResultadoExamen'
        db.delete_table(u'historias_app_resultadoexamen')


    models = {
        u'historias_app.examen': {
            'Meta': {'object_name': 'Examen'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'historia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['historias_app.Historia']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'historias_app.historia': {
            'Meta': {'object_name': 'Historia'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo_consulta': ('django.db.models.fields.TextField', [], {}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pacientes_app.Paciente']"})
        },
        u'historias_app.resultadoexamen': {
            'Meta': {'ordering': "['fecha']", 'object_name': 'ResultadoExamen'},
            'examen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['historias_app.Examen']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_resultado_examen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['historias_app.TipoResultadoExamen']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'historias_app.tiporesultadoexamen': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'TipoResultadoExamen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_dato': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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

    complete_apps = ['historias_app']