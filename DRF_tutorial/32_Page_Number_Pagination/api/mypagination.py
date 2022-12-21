from rest_framework.pagination import PageNumberPagination

class Mypagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'p'
    page_size_query_param = 'record'
    max_page_size = 7
    last_page_strings = 'end'
