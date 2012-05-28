# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Corporation'
        db.create_table('corpos_corporation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('capacity_information', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('capacity_datasteal', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('capacity_sabotage', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('capacity_scandal', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('capacity_protection', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('political_position', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length='12')),
            ('rank', self.gf('django.db.models.fields.CharField')(max_length='3')),
            ('on_first', self.gf('django.db.models.fields.TextField')()),
            ('on_first_effect', self.gf('django.db.models.fields.TextField')()),
            ('on_last', self.gf('django.db.models.fields.TextField')()),
            ('on_last_effect', self.gf('django.db.models.fields.TextField')()),
            ('on_crash', self.gf('django.db.models.fields.TextField')()),
            ('on_crash_effect', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('corpos', ['Corporation'])

        # Adding model 'Asset'
        db.create_table('corpos_asset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('turn', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corpos.Corporation'])),
            ('value', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('corpos', ['Asset'])


    def backwards(self, orm):
        # Deleting model 'Corporation'
        db.delete_table('corpos_corporation')

        # Deleting model 'Asset'
        db.delete_table('corpos_asset')


    models = {
        'corpos.asset': {
            'Meta': {'object_name': 'Asset'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corpos.Corporation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'turn': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'value': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'corpos.corporation': {
            'Meta': {'object_name': 'Corporation'},
            'capacity_datasteal': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_information': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_protection': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_sabotage': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_scandal': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'on_crash': ('django.db.models.fields.TextField', [], {}),
            'on_crash_effect': ('django.db.models.fields.TextField', [], {}),
            'on_first': ('django.db.models.fields.TextField', [], {}),
            'on_first_effect': ('django.db.models.fields.TextField', [], {}),
            'on_last': ('django.db.models.fields.TextField', [], {}),
            'on_last_effect': ('django.db.models.fields.TextField', [], {}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': "'12'"}),
            'political_position': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': "'3'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['corpos']