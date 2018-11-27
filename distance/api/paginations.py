from rest_framework.pagination import PageNumberPagination


class DistancePagination(PageNumberPagination):
    page_size = 10
