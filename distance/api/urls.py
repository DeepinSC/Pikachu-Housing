from distance.api.views import DistanceViewSet
from distance.api import views
from rest_framework.urlpatterns import format_suffix_patterns

distance_list = DistanceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

distance_detail = DistanceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

close_house_detail = ClosestHouseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
	url(r'^$', views.api_root, name='api_root'),
	url(r'^distance/$', distance_list, name='distance-list'),
	url(r'^distance/(?P<pk>[0-9]+)/$', distance_detail, name='distance-detail'),
	url(r'^house/department/(?P<pk>[0-9]+)/$', close_house_list, name='close-house-list'),
])