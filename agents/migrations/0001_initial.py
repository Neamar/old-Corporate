# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fixer'
        db.create_table('agents_fixer', (
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
            ('friend', self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True)),
            ('foe', self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='10', null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length='50')),
        ))
        db.send_create_signal('agents', ['Fixer'])

        # Adding model 'Yakuza'
        db.create_table('agents_yakuza', (
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
            ('friend', self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True)),
            ('foe', self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='10', null=True, blank=True)),
            ('foster_type', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('foster_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['joueurs.Player'], null=True, blank=True)),
        ))
        db.send_create_signal('agents', ['Yakuza'])

        # Adding model 'Agency'
        db.create_table('agents_agency', (
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
            ('friend', self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True)),
            ('foe', self.gf('django.db.models.fields.CharField')(max_length='200', null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length='10', null=True, blank=True)),
        ))
        db.send_create_signal('agents', ['Agency'])


    def backwards(self, orm):
        # Deleting model 'Fixer'
        db.delete_table('agents_fixer')

        # Deleting model 'Yakuza'
        db.delete_table('agents_yakuza')

        # Deleting model 'Agency'
        db.delete_table('agents_agency')


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
            'description': ('django.db.models.fields.TextField', [], {}),
            'honor': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'pc': ('django.db.models.fields.CharField', [], {'max_length': "'15'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['agents']