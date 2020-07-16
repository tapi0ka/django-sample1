# Generated by Django 3.0.8 on 2020-07-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExecList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exec_method', models.CharField(max_length=100, verbose_name='処理種別')),
                ('process_status', models.CharField(max_length=100, verbose_name='状態')),
                ('begin_at', models.DateTimeField(verbose_name='開始日時')),
                ('end_at', models.DateTimeField(verbose_name='終了日時')),
            ],
            options={
                'db_table': 'snsexeclist',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitter', models.CharField(max_length=200, verbose_name='提出者')),
                ('submission_year_month', models.CharField(max_length=200, verbose_name='提出年月')),
                ('work_place', models.CharField(max_length=200, verbose_name='作業場所')),
                ('work_content', models.CharField(max_length=200, verbose_name='作業内容')),
                ('environment', models.CharField(max_length=200, verbose_name='環境')),
                ('problem', models.CharField(max_length=200, verbose_name='問題点')),
                ('self_assessment', models.CharField(max_length=200, verbose_name='自己評価')),
                ('acquisition_skill', models.CharField(max_length=200, verbose_name='習得スキル')),
                ('work_schedule', models.CharField(max_length=200, verbose_name='作業予定')),
                ('goal', models.CharField(max_length=200, verbose_name='目標')),
                ('other', models.CharField(max_length=200, verbose_name='その他')),
                ('created_at', models.CharField(max_length=200, verbose_name='作成日時')),
                ('updated_at', models.CharField(max_length=200, verbose_name='更新日時')),
            ],
            options={
                'db_table': 'reports',
            },
        ),
    ]