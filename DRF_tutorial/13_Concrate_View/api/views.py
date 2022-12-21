from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer

from rest_framework.generics import (
        ListAPIView,
        CreateAPIView, 
        UpdateAPIView,
        RetrieveAPIView, 
        DestroyAPIView , 
        ListCreateAPIView, 
        RetrieveDestroyAPIView, 
        RetrieveUpdateDestroyAPIView, 
        RetrieveUpdateAPIView
        )



# class StudentList(ListAPIView):
#     serializer_class = StudentSerializer
#     queryset =Student.objects.all()
   
# class StudentCreate(CreateAPIView):
#     serializer_class = StudentSerializer
#     queryset =Student.objects.all()

# class StudentUpdate(UpdateAPIView):
#     serializer_class = StudentSerializer
#     queryset =Student.objects.all()


# class StudentRetrieve(RetrieveAPIView):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer
    

# class StudentDestroy(DestroyAPIView):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer

# #  combination --------

# class Student_getall_post(ListCreateAPIView):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer

# class Student_get_del(RetrieveDestroyAPIView):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer

# class Student_get_up_del(RetrieveUpdateDestroyAPIView):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer

# class Student_get_up(RetrieveUpdateAPIView):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer


# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
#  one url all in one ----------------------------------------------------------------------
class StudentAPI(ListCreateAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer

class StudentAPI_pk(RetrieveUpdateDestroyAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
