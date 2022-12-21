from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   
# three method to generate token
    # 1. By Admin Pannel
    # 2. By Command - python manage.py drf_create_token username
    # 3. By exposing API
            # is showed in this project
            # and in project 22
    # 4. Signals in project 23

    
    