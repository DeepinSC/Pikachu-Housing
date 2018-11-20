from rest_framework import viewsets
from provider.models import Provider
from provider.api.paginations import ProviderPagination
from serializers import ProviderSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@permission_classes((IsAuthenticatedOrReadOnly,))
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    pagination_class = ProviderPagination
    serializer_class = ProviderSerializer
