from rest_framework.pagination import PageNumberPagination


class DepartmentPagination(PageNumberPagination):
    page_size = 10
