from rest_framework.pagination import LimitOffsetPagination

class Mypagination(LimitOffsetPagination):
   default_limit =5 
   max_limit = 7
   limit_query_param = 'r'
   offset_query_param = 'off'
