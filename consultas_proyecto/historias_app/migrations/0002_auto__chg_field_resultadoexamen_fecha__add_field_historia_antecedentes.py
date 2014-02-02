# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ResultadoExamen.fecha'
        db.alter_column(u'historias_app_resultadoexamen', 'fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Adding field 'Historia.antecedentes_personales'
        db.add_column(u'historias_app_historia', 'antecedentes_personales',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.antecedentes_familiares'
        db.add_column(u'historias_app_historia', 'antecedentes_familiares',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.habitos_psicobiologicos'
        db.add_column(u'historias_app_historia', 'habitos_psicobiologicos',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_general'
        db.add_column(u'historias_app_historia', 'examen_general',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_piel'
        db.add_column(u'historias_app_historia', 'examen_piel',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_cabeza'
        db.add_column(u'historias_app_historia', 'examen_cabeza',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_ojos'
        db.add_column(u'historias_app_historia', 'examen_ojos',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_oidos'
        db.add_column(u'historias_app_historia', 'examen_oidos',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_nariz'
        db.add_column(u'historias_app_historia', 'examen_nariz',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_boca'
        db.add_column(u'historias_app_historia', 'examen_boca',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_garganta'
        db.add_column(u'historias_app_historia', 'examen_garganta',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_respiratorio'
        db.add_column(u'historias_app_historia', 'examen_respiratorio',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_osteomuscular'
        db.add_column(u'historias_app_historia', 'examen_osteomuscular',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_cardiovasuclar'
        db.add_column(u'historias_app_historia', 'examen_cardiovasuclar',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_gastrointestinal'
        db.add_column(u'historias_app_historia', 'examen_gastrointestinal',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_genitourinario'
        db.add_column(u'historias_app_historia', 'examen_genitourinario',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_ginecologico'
        db.add_column(u'historias_app_historia', 'examen_ginecologico',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_nervioso_y_mental'
        db.add_column(u'historias_app_historia', 'examen_nervioso_y_mental',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.examen_epidemiologico'
        db.add_column(u'historias_app_historia', 'examen_epidemiologico',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Historia.temperatura'
        db.add_column(u'historias_app_historia', 'temperatura',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Historia.pulso'
        db.add_column(u'historias_app_historia', 'pulso',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Historia.respiracion'
        db.add_column(u'historias_app_historia', 'respiracion',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Historia.tension_art_sist'
        db.add_column(u'historias_app_historia', 'tension_art_sist',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Historia.tension_art_diast'
        db.add_column(u'historias_app_historia', 'tension_art_diast',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Historia.frecuencia_cardiaca'
        db.add_column(u'historias_app_historia', 'frecuencia_cardiaca',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Historia.peso'
        db.add_column(u'historias_app_historia', 'peso',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Historia.talla'
        db.add_column(u'historias_app_historia', 'talla',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Historia.grasa_corporal'
        db.add_column(u'historias_app_historia', 'grasa_corporal',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True),
                      keep_default=False)


        # Changing field 'Examen.fecha_creacion'
        db.alter_column(u'historias_app_examen', 'fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'ResultadoExamen.fecha'
        db.alter_column(u'historias_app_resultadoexamen', 'fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))
        # Deleting field 'Historia.antecedentes_personales'
        db.delete_column(u'historias_app_historia', 'antecedentes_personales')

        # Deleting field 'Historia.antecedentes_familiares'
        db.delete_column(u'historias_app_historia', 'antecedentes_familiares')

        # Deleting field 'Historia.habitos_psicobiologicos'
        db.delete_column(u'historias_app_historia', 'habitos_psicobiologicos')

        # Deleting field 'Historia.examen_general'
        db.delete_column(u'historias_app_historia', 'examen_general')

        # Deleting field 'Historia.examen_piel'
        db.delete_column(u'historias_app_historia', 'examen_piel')

        # Deleting field 'Historia.examen_cabeza'
        db.delete_column(u'historias_app_historia', 'examen_cabeza')

        # Deleting field 'Historia.examen_ojos'
        db.delete_column(u'historias_app_historia', 'examen_ojos')

        # Deleting field 'Historia.examen_oidos'
        db.delete_column(u'historias_app_historia', 'examen_oidos')

        # Deleting field 'Historia.examen_nariz'
        db.delete_column(u'historias_app_historia', 'examen_nariz')

        # Deleting field 'Historia.examen_boca'
        db.delete_column(u'historias_app_historia', 'examen_boca')

        # Deleting field 'Historia.examen_garganta'
        db.delete_column(u'historias_app_historia', 'examen_garganta')

        # Deleting field 'Historia.examen_respiratorio'
        db.delete_column(u'historias_app_historia', 'examen_respiratorio')

        # Deleting field 'Historia.examen_osteomuscular'
        db.delete_column(u'historias_app_historia', 'examen_osteomuscular')

        # Deleting field 'Historia.examen_cardiovasuclar'
        db.delete_column(u'historias_app_historia', 'examen_cardiovasuclar')

        # Deleting field 'Historia.examen_gastrointestinal'
        db.delete_column(u'historias_app_historia', 'examen_gastrointestinal')

        # Deleting field 'Historia.examen_genitourinario'
        db.delete_column(u'historias_app_historia', 'examen_genitourinario')

        # Deleting field 'Historia.examen_ginecologico'
        db.delete_column(u'historias_app_historia', 'examen_ginecologico')

        # Deleting field 'Historia.examen_nervioso_y_mental'
        db.delete_column(u'historias_app_historia', 'examen_nervioso_y_mental')

        # Deleting field 'Historia.examen_epidemiologico'
        db.delete_column(u'historias_app_historia', 'examen_epidemiologico')

        # Deleting field 'Historia.temperatura'
        db.delete_column(u'historias_app_historia', 'temperatura')

        # Deleting field 'Historia.pulso'
        db.delete_column(u'historias_app_historia', 'pulso')

        # Deleting field 'Historia.respiracion'
        db.delete_column(u'historias_app_historia', 'respiracion')

        # Deleting field 'Historia.tension_art_sist'
        db.delete_column(u'historias_app_historia', 'tension_art_sist')

        # Deleting field 'Historia.tension_art_diast'
        db.delete_column(u'historias_app_historia', 'tension_art_diast')

        # Deleting field 'Historia.frecuencia_cardiaca'
        db.delete_column(u'historias_app_historia', 'frecuencia_cardiaca')

        # Deleting field 'Historia.peso'
        db.delete_column(u'historias_app_historia', 'peso')

        # Deleting field 'Historia.talla'
        db.delete_column(u'historias_app_historia', 'talla')

        # Deleting field 'Historia.grasa_corporal'
        db.delete_column(u'historias_app_historia', 'grasa_corporal')


        # Changing field 'Examen.fecha_creacion'
        db.alter_column(u'historias_app_examen', 'fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

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
            'examen_cardiovasuclar': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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