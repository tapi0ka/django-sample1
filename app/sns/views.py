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

from sns.services import login, get_report_urls, open_report_detail

from jinjer.serializers import MainListSerializer
from jinjer.serializers import SubListSerializer
from jinjer.serializers import ExecListSerializer

from jinjer.models import ExecList
from jinjer.models import MainList
from jinjer.models import SubList
from jinjer.models import ErrorLog



def index(request):
    print("aaaa")
    return render(request, 'sns/index.html')

class GetReportViewSet(viewsets.ModelViewSet):
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
        request.data['YMD'] = '202005'

        # dict形式のデータをシリアライザにぶっこむ
        serializer = self.get_serializer(data=request.data)

        # シリアライザにぶっこんだdictが問題ないかチェック
        serializer.is_valid(raise_exception=True)

        try:
            print('start')
            driver = webdriver.Chrome(options=get_options())
            login(driver)
            # report_url_list = get_report_urls(driver, request.data['YMD'])
            # for item in report_url_list:
            open_report_detail(driver, 'https://sv27.wadax.ne.jp/~stylagy-co-jp/sns/?m=pc&a=page_h_report_m_show&id=12324')
            # open_report_detail(driver, item)
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
