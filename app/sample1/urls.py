from django.urls import path
from django.conf.urls import include, url

from .views import index

app_name = "sample1"
urlpatterns = [
    path('', index, name='index'),
    # path('checkin/', CheckInViewSet.as_view(), name='token_obtain_pair'),
    # url(r'^mainlist/', MainListViewSet.as_view(), name='token_obtain_pair'),
    # path('sublist/', SubListViewSet.as_view(), name='token_refresh'),
]

