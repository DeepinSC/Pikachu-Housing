from department.api.views import DepartmentViewSet
from department.api import views
from rest_framework.urlpatterns import format_suffix_patterns

department_list = DepartmentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

department_detail = DepartmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root, name='api_root'),
    url(r'^department/$', department_list, name='department-list'),
    url(r'^department/(?P<pk>[0-9]+)/$', department_detail, name='department-detail'),
]) 