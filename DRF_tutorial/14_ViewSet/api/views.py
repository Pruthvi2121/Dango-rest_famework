from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets


# Create your views here.


class StudentAPI_ViewSet(viewsets.ViewSet):

    def list(self, request):
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk = None):

        id = pk
        if id is not None:
            std = Student.objects.get(id=id)
            serializer = StudentSerializer(std)
            return Response(serializer.data, status=status.HTTP_200_OK)

        

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created '} ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self , request, pk):
    
        id = pk
        std = Student.objects.get(id = id)
        serializer = StudentSerializer(std, data= request.data )
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data Updated '} ,status=status.HTTP_200_OK)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        id = pk
        std = Student.objects.get(id = id)
        serializer = StudentSerializer(std, data= request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data Updated '} ,status=status.HTTP_200_OK)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        id = pk
        std = Student.objects.get(id=id)
        std.delete()
        return Response({'msg':'success deleted '} ,status=status.HTTP_200_OK)
        # thi