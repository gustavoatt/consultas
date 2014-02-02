# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Historia.examen_cardiovasuclar'
        db.delete_column(u'historias_app_historia', 'examen_cardiovasuclar')

        # Adding field 'Historia.examen_cardiovascular'
        db.add_column(u'historias_app_historia', 'examen_cardiovascular',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Historia.examen_cardiovasuclar'
        db.add_column(u'historias_app_historia', 'examen_cardiovasuclar',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Historia.examen_cardiovascular'
        db.delete_column(u'historias_app_historia', 'examen_cardiovascular')


    models = {
        u'historias_app.examen': {
            'Meta': {'object_name': 'Examen'},
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'historia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['historias_app.Historia']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'historias_app.historia': {
            'Meta': {'object_name': 'Historia'},
            'antecedentes_familiares': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'antecedentes_personales': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_boca': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_cabeza': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_cardiovascular': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_epidemiologico': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_garganta': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_gastrointestinal': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_general': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_genitourinario': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_ginecologico': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_nariz': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_nervioso_y_mental': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_oidos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_ojos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_osteomuscular': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_piel': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'examen_respiratorio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'frecuencia_cardiaca': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'grasa_corporal': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'habitos_psicobiologicos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo_consulta': ('django.db.models.fields.TextField', [], {}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pacientes_app.Paciente']"}),
            'peso': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'pulso': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'respiracion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'talla': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'temperatura': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'tension_art_diast': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tension_art_sist': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'historias_app.resultadoexamen': {
            'Meta': {'ordering': "['fecha']", 'object_name': 'ResultadoExamen'},
            'examen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['historias_app.Examen']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono_casa': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['historias_app']