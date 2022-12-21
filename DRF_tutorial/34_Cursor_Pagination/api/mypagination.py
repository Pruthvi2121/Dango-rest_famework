from rest_framework.pagination import CursorPagination

class Mypagination(CursorPagination):
   page_size=3
   ordering = 'name'
   cursor_query_param = 'c'