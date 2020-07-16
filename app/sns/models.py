import uuid
from django.db import models
from django.utils import timezone

# Create your models here.

class ExecList(models.Model):
    '''
    処理日時リスト
    '''
    class Meta:
        #テーブル名設定
        db_table = 'snsexeclist'

    #フィールド設定(サブ項目名、総数)
    exec_method = models.CharField(verbose_name='処理種別', max_length=100)
    process_status = models.CharField(verbose_name='状態', max_length=100)
    begin_at = models.DateTimeField(verbose_name="開始日時")
    end_at = models.DateTimeField(verbose_name="終了日時")

    #名称設定
    def __str__(self):
        return self.begin_at

class Reports(models.Model):
    '''
    処理日時リスト
    '''
    class Meta:
        #テーブル名設定
        db_table = 'reports'

    # id = models.CharField(max_length=10, primary_key=True)
    submitter = models.CharField(verbose_name='提出者', max_length=200)
    submission_year_month = models.CharField(verbose_name='提出年月', max_length=200)
    work_place = models.CharField(verbose_name='作業場所', max_length=200)
    work_content = models.CharField(verbose_name='作業内容', max_length=200)
    environment = models.CharField(verbose_name='環境', max_length=200)
    problem = models.CharField(verbose_name='問題点', max_length=200)
    self_assessment = models.CharField(verbose_name='自己評価', max_length=200)
    acquisition_skill = models.CharField(verbose_name='習得スキル', max_length=200)
    work_schedule = models.CharField(verbose_name='作業予定', max_length=200)
    goal = models.CharField(verbose_name='目標', max_length=200)
    other = models.CharField(verbose_name='その他', max_length=200)
    created_at = models.CharField(verbose_name='作成日時', max_length=200)
    updated_at = models.CharField(verbose_name='更新日時', max_length=200)

    #フィールド設定(サブ項目名、総数)
    # exec_method = models.CharField(verbose_name='処理種別', max_length=100)
    # process_status = models.CharField(verbose_name='状態', max_length=100)
    # begin_at = models.DateTimeField(verbose_name="開始日時")
    # end_at = models.DateTimeField(verbose_name="終了日時")

    #名称設定
    def __str__(self):
        return self.submitter