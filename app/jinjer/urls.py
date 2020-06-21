'''
Jinjer Url Path
'''
from django.urls import path
from django.conf.urls import include, url

from rest_framework import routers

from .views import MainListViewSet, SubListViewSet, CheckInViewSet, CheckOutViewSet, index

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'mainlist', MainListViewSet)
router.register(r'sublist', SubListViewSet)
router.register(r'checkin', CheckInViewSet)
router.register(r'checkout', CheckOutViewSet)

app_name = "jinjer"
urlpatterns = [
    path('', index),
    url(r'^', include(router.urls)),
]
