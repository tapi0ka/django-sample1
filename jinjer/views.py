"""This is a est program."""
import os
import importlib
import time

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from selenium import webdriver

from jinjer.services import login, clockingIn, clockingOut

from jinjer.serializers import MainListSerializer
from jinjer.serializers import SubListSerializer
from jinjer.serializers import ExecListSerializer

from jinjer.models import ExecList
from jinjer.models import MainList
from jinjer.models import SubList
from jinjer.models import ErrorLog


class MainListViewSet(viewsets.ModelViewSet):
    queryset = MainList.objects.all()
    serializer_class = MainListSerializer
    #認証済のみアクセス可能
    permission_classes = [IsAuthenticated]


class SubListViewSet(viewsets.ModelViewSet):
    queryset = SubList.objects.all()
    serializer_class = SubListSerializer
    #認証済のみアクセス可能
    permission_classes = [IsAuthenticated]


class CheckInViewSet(viewsets.ModelViewSet):
    # http_method_names = ['post']
    # queryset = get_exec()
    queryset = ExecList.objects.all()
    serializer_class = ExecListSerializer
    permission_classes = [IsAuthenticated]

    # lookup_field = 'slug'

    # @action(detail=False, methods=['post'])
    # def set_password(self, request, pk=None):
    #     print("aaa")
    #     exec = self.get_object()
    #     serializer = ExecListSerializer(data=request.data)
    #     pass
    # return Response("aaa")
    # return Response("error", status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            driver = webdriver.Chrome(options=get_options())
            login(driver)
            clockingIn(driver)
            # raise NameError('HiThere')
        except Exception as ex:
            ErrorLog(user_id="takashi",
                     event_id=1,
                     message="{}_seleniumでエラー発生".format(ex)).save()
        finally:
            driver.close()

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


def get_options():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
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
