'''
Jinjer Url Path
'''
from django.urls import path
from django.conf.urls import include, url

from rest_framework import routers

from .views import index, GetReportViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'getreport', GetReportViewSet)
# router.register(r'checkout', CheckOutViewSet)

app_name = "sns"
urlpatterns = [
    path('', index),
    url(r'^', include(router.urls)),
]
