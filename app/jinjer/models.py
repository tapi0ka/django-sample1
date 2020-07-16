import uuid
from django.db import models
from django.utils import timezone

#メインリストテーブル
class MainList(models.Model):
    class Meta:
        #テーブル名設定
        db_table = 'mainlist'

    #フィールド設定(メイン項目名、日付)
    title = models.CharField(verbose_name='メイン項目名', max_length=100)
    datetime = models.DateTimeField(verbose_name='日付')

    #名称設定
    def __str__(self):
        return self.title


#サブリストテーブル
class SubList(models.Model):
    class Meta:
        #テーブル名設定
        db_table = 'sublist'

    #フィールド設定(サブ項目名、総数)
    mainlist = models.ForeignKey(MainList, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='サブ項目名', max_length=100)
    totalnum = models.IntegerField(verbose_name='総数', default=0)

    #名称設定
    def __str__(self):
        return self.title


#サブリストテーブル
class AcountList(models.Model):
    class Meta:
        #テーブル名設定
        db_table = 'acountlist'

    #フィールド設定(サブ項目名、総数)
    business_id = models.IntegerField(verbose_name="企業ID")
    employee_id = models.CharField(verbose_name='社員番号', max_length=100)
    password = models.CharField(verbose_name='パスワード', max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    #名称設定
    def __str__(self):
        return self.employee_id


class ExecList(models.Model):
    '''
    処理日時リスト
    '''
    class Meta:
        #テーブル名設定
        db_table = 'execlist'

    #フィールド設定(サブ項目名、総数)
    exec_method = models.CharField(verbose_name='処理種別', max_length=100)
    process_status = models.CharField(verbose_name='状態', max_length=100)
    begin_at = models.DateTimeField(verbose_name="開始日時")
    end_at = models.DateTimeField(verbose_name="終了日時")

    #名称設定
    def __str__(self):
        return self.begin_at


class ErrorLog(models.Model):
    class Meta:
        db_table = 'error_log'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(verbose_name='ユーザID', max_length=100)
    event_id = models.IntegerField()
    message = models.CharField(verbose_name='詳細', max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    #名称設定
    def __str__(self):
        return str(self.created_at)