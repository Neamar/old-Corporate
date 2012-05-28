# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.influence'
        db.add_column('joueurs_player', 'influence',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Player.political_strength'
        db.add_column('joueurs_player', 'political_strength',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.political_position'
        db.add_column('joueurs_player', 'political_position',
                      self.gf('django.db.models.fields.CharField')(default='nc', max_length=16),
                      keep_default=False)

        # Adding field 'Player.creation_constraints'
        db.add_column('joueurs_player', 'creation_constraints',
                      self.gf('django.db.models.fields.TextField')(default='Gaijin'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.influence'
        db.delete_column('joueurs_player', 'influence')

        # Deleting field 'Player.political_strength'
        db.delete_column('joueurs_player', 'political_strength')

        # Deleting field 'Player.political_position'
        db.delete_column('joueurs_player', 'political_position')

        # Deleting field 'Player.creation_constraints'
        db.delete_column('joueurs_player', 'creation_constraints')


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
            'creation_constraints': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'honor': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influence': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'pc': ('django.db.models.fields.CharField', [], {'max_length': "'15'"}),
            'political_position': ('django.db.models.fields.CharField', [], {'default': "'nc'", 'max_length': '16'}),
            'political_strength': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
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