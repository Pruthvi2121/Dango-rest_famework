from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from rest_framework.filters import OrderingFilter
class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends =[OrderingFilter]
    # ordering_fields = ['name']   
    ordering_fields = ['name', 'city']   
    