from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPaginationClass(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {'count': self.page.paginator.count,
             'navigation': {
                 'next': self.get_next_link(),
                 'previous': self.get_previous_link(),
                 'limit': self.page_size,
             },
             'results': data})
