from django.urls import include, path
from rest_framework import routers

from api.views import CategoryViewSet, GoodViewSet, UserViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='category')
router_v1.register('goods', GoodViewSet, basename='good')
router_v1.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
