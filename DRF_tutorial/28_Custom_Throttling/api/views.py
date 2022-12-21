from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer

from rest_framework.generics import (
        ListAPIView,
        CreateAPIView, 
        UpdateAPIView,
        RetrieveAPIView, 
        DestroyAPIView , 

     )


from rest_framework.throttling import ScopedRateThrottle


class StudentList(ListAPIView):
    serializer_class = StudentSerializer
    queryset =Student.objects.all()

    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'list'
   
class StudentCreate(CreateAPIView):
    serializer_class = StudentSerializer
    queryset =Student.objects.all()

    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'create'

class StudentUpdate(UpdateAPIView):
    serializer_class = StudentSerializer
    queryset =Student.objects.all()

    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'update'


class StudentRetrieve(RetrieveAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'list'
    

class StudentDestroy(DestroyAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer


    throttle_classes=[ScopedRateThrottle]
    throttle_scope = 'destroy'

