from rest_framework import pagination

class LargeResultPagination(pagination.PageNumberPagination):
    page_size = None
    