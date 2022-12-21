from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
# Create your views here.


from rest_framework.generics import ListAPIView
from .mypagination import Mypagination
class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = Mypagination
    