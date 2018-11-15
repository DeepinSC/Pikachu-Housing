from housing.api.views import HouseViewSet
from housing.api import views
from rest_framework.urlpatterns import format_suffix_patterns

house_list = HouseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

house_detail = HouseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root, name='api_root'),
    url(r'^house/$', house_list, name='house-list'),
    url(r'^house/(?P<pk>[0-9]+)/$', house_detail, name='house-detail'),
]) 