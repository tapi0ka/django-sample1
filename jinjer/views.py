from rest_framework import viewsets

#パーミッション設定
from rest_framework.permissions import IsAuthenticated

from .models import MainList
from .models import SubList
from .serializers import MainListSerializer
from .serializers import SubListSerializer
from django.http.response import HttpResponse
from django.urls import reverse
from jinjer.serializers import ExecListSerializer
from jinjer.models import ExecList


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
    http_method_names = ['post']
    queryset = ExecList.objects.all()
    serializer_class = ExecListSerializer
    permission_classes = [IsAuthenticated]


def index(request):
    # urlName = reverse('index')
    return HttpResponse("Hello, world. You're at the polls index.")