# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Agency.private_friend'
        db.add_column('agents_agency', 'private_friend',
                      self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Agency.private_foe'
        db.add_column('agents_agency', 'private_foe',
                      self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Yakuza.private_friend'
        db.add_column('agents_yakuza', 'private_friend',
                      self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Yakuza.private_foe'
        db.add_column('agents_yakuza', 'private_foe',
                      self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fixer.private_friend'
        db.add_column('agents_fixer', 'private_friend',
                      self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Fixer.private_foe'
        db.add_column('agents_fixer', 'private_foe',
                      self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Agency.private_friend'
        db.delete_column('agents_agency', 'private_friend')

        # Deleting field 'Agency.private_foe'
        db.delete_column('agents_agency', 'private_foe')

        # Deleting field 'Yakuza.private_friend'
        db.delete_column('agents_yakuza', 'private_friend')

        # Deleting field 'Yakuza.private_foe'
        db.delete_column('agents_yakuza', 'private_foe')

        # Deleting field 'Fixer.private_friend'
        db.delete_column('agents_fixer', 'private_friend')

        # Deleting field 'Fixer.private_foe'
        db.delete_column('agents_fixer', 'private_foe')


    models = {
        'agents.agency': {
            'Meta': {'object_name': 'Agency'},
            'capacity_datasteal': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_information': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_protection': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_sabotage': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_scandal': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'foe': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'friend': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'private_foe': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'private_friend': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'10'", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'agents.fixer': {
            'Meta': {'object_name': 'Fixer'},
            'capacity_datasteal': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_information': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_protection': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_sabotage': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_scandal': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'foe': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'friend': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'private_foe': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'private_friend': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'10'", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'agents.yakuza': {
            'Meta': {'object_name': 'Yakuza'},
            'capacity_datasteal': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_information': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_protection': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_sabotage': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'capacity_scandal': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'foe': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'foster_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['joueurs.Player']", 'null': 'True', 'blank': 'True'}),
            'foster_type': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'friend': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'private_foe': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'private_friend': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': "'10'", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
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
        },
        'joueurs.player': {
            'Meta': {'object_name': 'Player'},
            'citizen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['corpos.Corporation']", 'null': 'True', 'blank': 'True'}),
            'creation_constraints': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'honor': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influence': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'pc': ('django.db.models.fields.CharField', [], {'max_length': "'15'"}),
            'political_position': ('django.db.models.fields.CharField', [], {'default': "'nc'", 'max_length': '16'}),
            'political_strength': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['agents']