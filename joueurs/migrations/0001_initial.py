# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table('joueurs_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('pc', self.gf('django.db.models.fields.CharField')(max_length='15')),
            ('honor', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('citizen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corpos.Corporation'], null=True, blank=True)),
        ))
        db.send_create_signal('joueurs', ['Player'])

        # Adding model 'Share'
        db.create_table('joueurs_share', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joueurs.Player'])),
            ('corporation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corpos.Corporation'])),
        ))
        db.send_create_signal('joueurs', ['Share'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table('joueurs_player')

        # Deleting model 'Share'
        db.delete_table('joueurs_share')


    models = {
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
        },
        'joueurs.player': {
            'Meta': {'object_name': 'Player'},
            'citizen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corpos.Corporation']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'honor': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'pc': ('django.db.models.fields.CharField', [], {'max_length': "'15'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'joueurs.share': {
            'Meta': {'object_name': 'Share'},
            'corporation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corpos.Corporation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joueurs.Player']"})
        }
    }

    complete_apps = ['joueurs']