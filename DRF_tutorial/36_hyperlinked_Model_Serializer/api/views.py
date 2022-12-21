from django.shortcuts import render

# Create your views here.

from .models import Student
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    