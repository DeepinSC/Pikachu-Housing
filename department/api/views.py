from rest_framework import viewsets
from department.models import Department
from department.api.paginations import DepartmentPagination
from serializers import DepartmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@permission_classes((IsAuthenticatedOrReadOnly,))
class DepartmentViewSet(viewsets.ModelViewSet):
    # pagination_class = DepartmentPagination
    serializer_class = DepartmentSerializer
    queryset = ''

    def list(self, request):
        queryset = Department.objects.raw('SELECT * FROM department_department')
        serializers = DepartmentSerializer(queryset, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk):
        queryset = Department.objects.raw('SELECT * FROM department_department WHERE department_department.id = %s',[pk])
        serializers = DepartmentSerializer(queryset, many=True)
        return Response(serializers.data)

