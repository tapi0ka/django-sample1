# Generated by Django 3.0.7 on 2020-06-14 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jinjer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcountList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.IntegerField(verbose_name='企業ID')),
                ('employee_id', models.CharField(max_length=100, verbose_name='社員番号')),
                ('password', models.CharField(max_length=100, verbose_name='パスワード')),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'acountlist',
            },
        ),
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
                'db_table': 'execlist',
            },
        ),
    ]