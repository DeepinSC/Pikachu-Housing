from rest_framework import viewsets
from department.models import Department
from department.api.paginations import DepartmentPagination
from serializers import DepartmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions

@permission_classes((IsAuthenticatedOrReadOnly,))
class DepartmentViewSet(viewsets.ModelViewSet):
    # pagination_class = DepartmentPagination
    pagination_class = DepartmentPagination
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.BasePermission,)

    def get_queryset(self):
        queryset = Department.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset
