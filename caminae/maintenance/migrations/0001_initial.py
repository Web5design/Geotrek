# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Intervention'
        db.create_table('interventions', (
            ('intervention_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('in_maintenance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('width', self.gf('django.db.models.fields.FloatField')()),
            ('height', self.gf('django.db.models.fields.FloatField')()),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('slope', self.gf('django.db.models.fields.IntegerField')()),
            ('material_cost', self.gf('django.db.models.fields.FloatField')()),
            ('heliport_cost', self.gf('django.db.models.fields.FloatField')()),
            ('subcontract_cost', self.gf('django.db.models.fields.FloatField')()),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.InterventionStatus'])),
            ('typology', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.InterventionTypology'], null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.Project'], null=True, blank=True)),
        ))
        db.send_create_signal('maintenance', ['Intervention'])

        # Adding M2M table for field disorders on 'Intervention'
        db.create_table('interventions_disorders', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('intervention', models.ForeignKey(orm['maintenance.intervention'], null=False)),
            ('interventiondisorder', models.ForeignKey(orm['maintenance.interventiondisorder'], null=False))
        ))
        db.create_unique('interventions_disorders', ['intervention_id', 'interventiondisorder_id'])

        # Adding model 'InterventionStatus'
        db.create_table('bib_de_suivi', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('code', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.TextField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['InterventionStatus'])

        # Adding model 'InterventionTypology'
        db.create_table('typologie_des_interventions', (
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('code', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('typology', self.gf('django.db.models.fields.TextField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['InterventionTypology'])

        # Adding model 'InterventionDisorder'
        db.create_table('desordres', (
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('code', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('disorder', self.gf('django.db.models.fields.TextField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['InterventionDisorder'])

        # Adding model 'InterventionJob'
        db.create_table('bib_fonctions', (
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('code', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.TextField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['InterventionJob'])

        # Adding model 'ManDay'
        db.create_table('journeeshomme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nb_days', self.gf('django.db.models.fields.IntegerField')()),
            ('intervention', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.Intervention'])),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.InterventionJob'])),
        ))
        db.send_create_signal('maintenance', ['ManDay'])

        # Adding model 'Project'
        db.create_table('chantiers', (
            ('project_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('begin_year', self.gf('django.db.models.fields.IntegerField')()),
            ('end_year', self.gf('django.db.models.fields.IntegerField')()),
            ('constraint', self.gf('django.db.models.fields.TextField')()),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('insert_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('project_owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='own', to=orm['maintenance.Organism'])),
            ('project_manager', self.gf('django.db.models.fields.related.ForeignKey')(related_name='manage', to=orm['maintenance.Organism'])),
        ))
        db.send_create_signal('maintenance', ['Project'])

        # Adding M2M table for field contractors on 'Project'
        db.create_table('chantiers_contractors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['maintenance.project'], null=False)),
            ('contractor', models.ForeignKey(orm['maintenance.contractor'], null=False))
        ))
        db.create_unique('chantiers_contractors', ['project_id', 'contractor_id'])

        # Adding model 'Contractor'
        db.create_table('prestataires', (
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('code', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('contractor', self.gf('django.db.models.fields.TextField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['Contractor'])

        # Adding model 'Organism'
        db.create_table('liste_de_tous_les_organismes', (
            ('code', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('organism', self.gf('django.db.models.fields.TextField')(max_length=128)),
        ))
        db.send_create_signal('maintenance', ['Organism'])

        # Adding model 'Funding'
        db.create_table('financement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authent.Structure'])),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.Project'])),
            ('organism', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maintenance.Organism'])),
        ))
        db.send_create_signal('maintenance', ['Funding'])


    def backwards(self, orm):
        # Deleting model 'Intervention'
        db.delete_table('interventions')

        # Removing M2M table for field disorders on 'Intervention'
        db.delete_table('interventions_disorders')

        # Deleting model 'InterventionStatus'
        db.delete_table('bib_de_suivi')

        # Deleting model 'InterventionTypology'
        db.delete_table('typologie_des_interventions')

        # Deleting model 'InterventionDisorder'
        db.delete_table('desordres')

        # Deleting model 'InterventionJob'
        db.delete_table('bib_fonctions')

        # Deleting model 'ManDay'
        db.delete_table('journeeshomme')

        # Deleting model 'Project'
        db.delete_table('chantiers')

        # Removing M2M table for field contractors on 'Project'
        db.delete_table('chantiers_contractors')

        # Deleting model 'Contractor'
        db.delete_table('prestataires')

        # Deleting model 'Organism'
        db.delete_table('liste_de_tous_les_organismes')

        # Deleting model 'Funding'
        db.delete_table('financement')


    models = {
        'authent.structure': {
            'Meta': {'object_name': 'Structure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'maintenance.contractor': {
            'Meta': {'object_name': 'Contractor', 'db_table': "'prestataires'"},
            'code': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'contractor': ('django.db.models.fields.TextField', [], {'max_length': '128'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.funding': {
            'Meta': {'object_name': 'Funding', 'db_table': "'financement'"},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organism': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.Organism']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.Project']"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.intervention': {
            'Meta': {'object_name': 'Intervention', 'db_table': "'interventions'"},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'disorders': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'interventions'", 'symmetrical': 'False', 'to': "orm['maintenance.InterventionDisorder']"}),
            'height': ('django.db.models.fields.FloatField', [], {}),
            'heliport_cost': ('django.db.models.fields.FloatField', [], {}),
            'in_maintenance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'intervention_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'jobs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['maintenance.InterventionJob']", 'through': "orm['maintenance.ManDay']", 'symmetrical': 'False'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'material_cost': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.Project']", 'null': 'True', 'blank': 'True'}),
            'slope': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.InterventionStatus']"}),
            'subcontract_cost': ('django.db.models.fields.FloatField', [], {}),
            'typology': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.InterventionTypology']", 'null': 'True', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.FloatField', [], {})
        },
        'maintenance.interventiondisorder': {
            'Meta': {'object_name': 'InterventionDisorder', 'db_table': "'desordres'"},
            'code': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'disorder': ('django.db.models.fields.TextField', [], {'max_length': '128'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.interventionjob': {
            'Meta': {'object_name': 'InterventionJob', 'db_table': "'bib_fonctions'"},
            'code': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.TextField', [], {'max_length': '128'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.interventionstatus': {
            'Meta': {'object_name': 'InterventionStatus', 'db_table': "'bib_de_suivi'"},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.TextField', [], {'max_length': '128'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"})
        },
        'maintenance.interventiontypology': {
            'Meta': {'object_name': 'InterventionTypology', 'db_table': "'typologie_des_interventions'"},
            'code': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['authent.Structure']"}),
            'typology': ('django.db.models.fields.TextField', [], {'max_length': '128'})
        },
        'maintenance.manday': {
            'Meta': {'object_name': 'ManDay', 'db_table': "'journeeshomme'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervention': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.Intervention']"}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['maintenance.InterventionJob']"}),
            'nb_days': ('django.db.models.fields.IntegerField', [], {})
        },
        'maintenance.organism': {
            'Meta': {'object_name': 'Organism', 'db_table': "'liste_de_tous_les_organismes'"},
            'code': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'organism': ('django.db.models.fields.TextField', [], {'max_length': '128'})
        },
        'maintenance.project': {
            'Meta': {'object_name': 'Project', 'db_table': "'chantiers'"},
            'begin_year': ('django.db.models.fields.IntegerField', [], {}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'constraint': ('django.db.models.fields.TextField', [], {}),
            'contractors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': "orm['maintenance.Contractor']"}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_year': ('django.db.models.fields.IntegerField', [], {}),
            'founders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['maintenance.Organism']", 'through': "orm['maintenance.Funding']", 'symmetrical': 'False'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'project_manager': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'manage'", 'to': "orm['maintenance.Organism']"}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'own'", 'to': "orm['maintenance.Organism']"}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['maintenance']