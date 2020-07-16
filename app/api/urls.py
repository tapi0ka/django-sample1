from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'
urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('jinjer/', include('jinjer.urls')),
    path('sns/', include('sns.urls'))
]
