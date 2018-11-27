from rest_framework.pagination import PageNumberPagination


class ProviderPagination(PageNumberPagination):
    page_size = 10
