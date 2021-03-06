# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Source1.Writing_Prompt_1'
        db.add_column('mydata_source1', 'Writing_Prompt_1',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_2'
        db.add_column('mydata_source1', 'Writing_Prompt_2',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_3'
        db.add_column('mydata_source1', 'Writing_Prompt_3',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_4'
        db.add_column('mydata_source1', 'Writing_Prompt_4',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_5'
        db.add_column('mydata_source1', 'Writing_Prompt_5',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_6'
        db.add_column('mydata_source1', 'Writing_Prompt_6',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_7'
        db.add_column('mydata_source1', 'Writing_Prompt_7',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_8'
        db.add_column('mydata_source1', 'Writing_Prompt_8',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_9'
        db.add_column('mydata_source1', 'Writing_Prompt_9',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_10'
        db.add_column('mydata_source1', 'Writing_Prompt_10',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_11'
        db.add_column('mydata_source1', 'Writing_Prompt_11',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_12'
        db.add_column('mydata_source1', 'Writing_Prompt_12',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_13'
        db.add_column('mydata_source1', 'Writing_Prompt_13',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Source1.Writing_Prompt_14'
        db.add_column('mydata_source1', 'Writing_Prompt_14',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Source1.Writing_Prompt_1'
        db.delete_column('mydata_source1', 'Writing_Prompt_1')

        # Deleting field 'Source1.Writing_Prompt_2'
        db.delete_column('mydata_source1', 'Writing_Prompt_2')

        # Deleting field 'Source1.Writing_Prompt_3'
        db.delete_column('mydata_source1', 'Writing_Prompt_3')

        # Deleting field 'Source1.Writing_Prompt_4'
        db.delete_column('mydata_source1', 'Writing_Prompt_4')

        # Deleting field 'Source1.Writing_Prompt_5'
        db.delete_column('mydata_source1', 'Writing_Prompt_5')

        # Deleting field 'Source1.Writing_Prompt_6'
        db.delete_column('mydata_source1', 'Writing_Prompt_6')

        # Deleting field 'Source1.Writing_Prompt_7'
        db.delete_column('mydata_source1', 'Writing_Prompt_7')

        # Deleting field 'Source1.Writing_Prompt_8'
        db.delete_column('mydata_source1', 'Writing_Prompt_8')

        # Deleting field 'Source1.Writing_Prompt_9'
        db.delete_column('mydata_source1', 'Writing_Prompt_9')

        # Deleting field 'Source1.Writing_Prompt_10'
        db.delete_column('mydata_source1', 'Writing_Prompt_10')

        # Deleting field 'Source1.Writing_Prompt_11'
        db.delete_column('mydata_source1', 'Writing_Prompt_11')

        # Deleting field 'Source1.Writing_Prompt_12'
        db.delete_column('mydata_source1', 'Writing_Prompt_12')

        # Deleting field 'Source1.Writing_Prompt_13'
        db.delete_column('mydata_source1', 'Writing_Prompt_13')

        # Deleting field 'Source1.Writing_Prompt_14'
        db.delete_column('mydata_source1', 'Writing_Prompt_14')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mydata7.common1': {
            'BirthDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'BirthMo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'BirthYr': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Class_Standing': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'College': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'College_Other': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Concentrate_Other': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology_EEB': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Biology_MCDB': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Chemistry': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Education': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Engineering': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Health': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Humanities': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__IDK': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Math': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Neurosci': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Other': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Physics': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Psych_BBCS': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Social_Science_not_Psych': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Concentrate__Stats': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Cum_GPA_Survey': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Declared': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'Employment': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'First_Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'High_School_CumGPA': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Greek': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Music_Art': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Other': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Religious': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Research': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Sports': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Involved_In__Volunteering': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Last_Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Common1', 'db_table': "'mydata_common1'"},
            'Other_Commitment': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'Parent_Ed': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'}),
            'Post_College': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'Semesters_Completed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uniqname': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'mydata7.emptysource': {
            'Meta': {'object_name': 'EmptySource'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        },
        'mydata7.source1': {
            'ACT_Math': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Another_Hard_Class': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'Attitude_Anxiety': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Attitude_Exams': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Attitude_Math': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Attitude_Physics_Exp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Attitude_Physics_Noexp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Confidence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Confidence_PreExam1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Confidence_PreExam2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Confidence_PreExam3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Confidence_PreFinal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Course': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Distribution_ID_135': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Distribution_ID_140': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Distribution_ID_235': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Distribution_ID_240': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'Exam_1_Score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_2_Score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_3_Score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Exam_Final_Score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_Grade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_Grade_Reset_initial': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_Grade_Reset_postexam1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_Grade_Reset_postexam2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_Grade_Reset_postexam3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam1_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam1_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam1_3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam2_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam2_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam2_3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam3_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam3_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreExam3_3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreFinal_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreFinal_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Goal_PreFinal_3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'GradeDistribution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'GradeDistribution_LeftShade': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'GradeDistribution_Peak': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'GradeDistribution_RightShade': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'HS_Activity': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'HS_Activity_Other': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'HS_Math': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'HS_Math_Other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Learner': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'MP_Name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'MP_PreExam_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'MP_PreExam_2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'MP_PreExam_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Source1', 'db_table': "'mydata_source1'"},
            'Movie': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'Movie_Other': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'Participation_PreExam_1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Participation_PreExam_2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Participation_PreExam_3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Partner': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'Past_Physics': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Past_Physics_Experience': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Past_Physics_When': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Pred_Grade_Exam1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Pred_Grade_Exam2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Pred_Grade_Exam3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Pred_Grade_Final': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Pred_Grade_Initial_135': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Pred_Grade_Initial_140': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Pred_Grade_Initial_235': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Pred_Grade_Initial_240': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Reason': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'Reflection_PreExam2_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Reflection_PreExam2_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Reflection_PreExam3_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Reflection_PreExam3_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Reflection_PreFinal_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Reflection_PreFinal_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'SAT_Math': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'SLC_Interest': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_10': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_11': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_12': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_13': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_14': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_4': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_5': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_6': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_7': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_8': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'Writing_Prompt_9': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'db_column': "'user_id'", 'on_delete': 'models.SET_NULL', 'to_field': "'username'", 'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['mydata7']