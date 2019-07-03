from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):

    page_size_query_param = 'pageSize'
    page_query_param = 'pageNo'

    max_page_size = 500

    def get_paginated_response(self, data):
        return Response({'result': {
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'totalPage': self.page.paginator.num_pages,
            'totalCount': self.page.paginator.count,
            'pageSize': 10,
            'pageNo': 0, 
            'data': data
        }})