from django.conf.urls import include, url

from .views import MainListViewSet, SubListViewSet, CheckInViewSet, CheckOutViewSet
from rest_framework import routers

# router = routers.DefaultRouter()
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'mainlist', MainListViewSet)
router.register(r'sublist', SubListViewSet)
router.register(r'checkin', CheckInViewSet)
router.register(r'checkout', CheckOutViewSet)

app_name = "jinjer"
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^/checkin/', CheckInViewSet.as_view())
    # path('', index, name='index'),
    # path('checkin/', CheckInViewSet.as_view(), name='token_obtain_pair'),
    # url(r'^mainlist/', MainListViewSet.as_view(), name='token_obtain_pair'),
    # path('sublist/', SubListViewSet.as_view(), name='token_refresh'),
]
