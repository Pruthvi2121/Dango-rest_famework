from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']

    #  method 1 : 
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)

    #  method 2 :

