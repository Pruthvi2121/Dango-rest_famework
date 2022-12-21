from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def StudentAPI(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            std = Student.objects.get(id=id)
            serializer = StudentSerializer(std)
            return Response(serializer.data, status=status.HTTP_200_OK)

        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created '} ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        std = Student.objects.get(id = id)
        serializer = StudentSerializer(std, data= request.data )
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data Updated '} ,status=status.HTTP_200_OK)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        id = request.data.get('id')
        std = Student.objects.get(id = id)
        serializer = StudentSerializer(std, data= request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data Updated '} ,status=status.HTTP_200_OK)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        std = Student.objects.get(id=id)
        std.delete()
        return Response({'msg':'success deleted '} ,status=status.HTTP_200_OK)
        