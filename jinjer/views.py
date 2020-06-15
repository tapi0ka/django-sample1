
#パーミッション設定

from .models import MainList
from .models import SubList
from .serializers import MainListSerializer
from .serializers import SubListSerializer
from django.http.response import HttpResponse
from django.urls import reverse
from jinjer.serializers import ExecListSerializer
from jinjer.models import ExecList

from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from jinjer.services import get_exec

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

    # @action(detail=False, methods=['get'])
    def aaa(self, request):
        return Response("aaa")

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
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def index(request):
    # urlName = reverse('index')
    return HttpResponse("Hello, world. You're at the polls index.")