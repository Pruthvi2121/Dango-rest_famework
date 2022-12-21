from rest_framework.permissions import BasePermission
from rest_framework.exceptions import MethodNotAllowed

class MyPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            raise MethodNotAllowed(f"{request.method} is not allowed pruthvi")