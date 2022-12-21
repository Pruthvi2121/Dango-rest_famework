from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from .CustomAuthentication import MyAuthentication
# from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# from .custompermission import MyPermission
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [MyAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [MyPermission]
   

    
    