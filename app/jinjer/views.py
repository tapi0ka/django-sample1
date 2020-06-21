"""This is a est program."""
import time
import chromedriver_binary

from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from selenium import webdriver

from jinjer.services import login, check_in, check_out

from jinjer.serializers import MainListSerializer
from jinjer.serializers import SubListSerializer
from jinjer.serializers import ExecListSerializer

from jinjer.models import ExecList
from jinjer.models import MainList
from jinjer.models import SubList
from jinjer.models import ErrorLog


def index(request):
    return render(request, 'jinjer/index.html')


class MainListViewSet(viewsets.ModelViewSet):
    '''
    サンプル
    '''
    queryset = MainList.objects.all()
    serializer_class = MainListSerializer
    #認証済のみアクセス可能
    permission_classes = [IsAuthenticated]


class SubListViewSet(viewsets.ModelViewSet):
    '''
    サンプル
    '''
    queryset = SubList.objects.all()
    serializer_class = SubListSerializer
    #認証済のみアクセス可能
    permission_classes = [IsAuthenticated]


class CheckInViewSet(viewsets.ModelViewSet):
    '''
    API /api/jinjer/checkin
    出勤打刻時のAPI
    '''
    queryset = ExecList.objects.all()
    serializer_class = ExecListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # 本当はクライアント側からContent-Type: application/jsonで投げるパラメータだけどめんどいから直接入れている
        request.data['exec_method'] = "checkin"
        request.data['process_status'] = "success"
        request.data['begin_at'] = timezone.now()
        request.data['end_at'] = timezone.now()

        # dict形式のデータをシリアライザにぶっこむ
        serializer = self.get_serializer(data=request.data)

        # シリアライザにぶっこんだdictが問題ないかチェック
        serializer.is_valid(raise_exception=True)

        try:
            driver = webdriver.Chrome(options=get_options())
            login(driver)
            # check_in(driver)
            # time.sleep(5)
        except Exception as ex:
            print('error')
            ErrorLog(user_id="takashi", event_id=1,
                     message="{}".format(ex)).save()
            # エラーのときは事項ステータスをエラーに変更
            request.data['process_status'] = 'error'
        finally:
            driver.close()

        request.data['end_at'] = timezone.now()
        serializer = self.get_serializer(data=request.data)

        # DBにデータインサート
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class CheckOutViewSet(viewsets.ModelViewSet):
    '''
    API /api/jinjer/checkout
    退勤打刻時のAPI
    '''
    queryset = ExecList.objects.all()
    serializer_class = ExecListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # 本当はクライアント側からContent-Type: application/jsonで投げるパラメータだけどめんどいから直接入れている
        request.data['exec_method'] = "checkout"
        request.data['process_status'] = "success"
        request.data['begin_at'] = timezone.now()
        request.data['end_at'] = timezone.now()

        # dict形式のデータをシリアライザにぶっこむ
        serializer = self.get_serializer(data=request.data)

        # シリアライザにぶっこんだdictが問題ないかチェック
        serializer.is_valid(raise_exception=True)

        try:
            driver = webdriver.Chrome(options=get_options())
            login(driver)
            check_out(driver)
        except Exception as ex:
            print('error')
            ErrorLog(user_id="takashi", event_id=2,
                     message="{}".format(ex)).save()
            # エラーのときは事項ステータスをエラーに変更
            request.data['process_status'] = 'error'
        finally:
            driver.close()

        request.data['end_at'] = timezone.now()
        serializer = self.get_serializer(data=request.data)

        # DBにデータインサート
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ヘッドレスモード
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1280x800')
    # options.add_argument('--disable-application-cache')
    # options.add_argument('--disable-infobars')
    # options.add_argument('--hide-scrollbars')
    # options.add_argument('--enable-logging')
    # options.add_argument('--log-level=0')
    # options.add_argument('--single-process')
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--homedir=/tmp')
    # options.binary_location = '/usr/bin/google-chrome'
    return options
