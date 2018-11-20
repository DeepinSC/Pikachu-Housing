from rest_framework import routers
from django.conf.urls import include, url, patterns
from housing.api.views import HouseViewSet
from distance.api.views import DistanceViewSet
from department.api.views import DepartmentViewSet
from provider.api.views import ProviderViewSet
from users.api.views import UserViewset

router = routers.DefaultRouter()
router.register(r'house', HouseViewSet, base_name='house')
router.register(r'provider', ProviderViewSet, base_name='provider')
router.register(r'distance', DistanceViewSet, base_name='distance')
router.register(r'department', DepartmentViewSet, base_name='department')
router.register(r'user', UserViewset, base_name='user')

app_name = 'api'

urlpatterns = patterns(
    'api',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)
