from rest_framework import serializers
#モデルインポート
from .models import MainList
from .models import SubList
from jinjer.models import ExecList


#メインリストシリアライザ
class MainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainList
        #取得フィールド設定
        fields = ('title', 'datetime')


#サブリストシリアライザ
class SubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubList
        #取得フィールド設定
        fields = ('title', 'totalnum')


class ExecListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecList
        #取得フィールド設定
        fields = ('exec_method', 'process_status', 'begin_at', 'end_at')
