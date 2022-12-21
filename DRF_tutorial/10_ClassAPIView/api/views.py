from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class StudentAPI(APIView):
    def get(self, request, pk = None ):
        if pk is not None:
            std = Student.objects.get(id = pk)
            serializer = StudentSerializer(std)
            return Response(serializer.data)
        std = Student.objects.all()
        serializer = StudentSerializer(std, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg : data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        std = Student.objects.get(id = pk)
        serializer = StudentSerializer(std, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg : Data updated '}, status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk): 
        std = Student.objects.get(id = pk)
        serializer = StudentSerializer(std, data = request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg :  Partial data updated '}, status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        std = Student.objects.get(id=pk)
        std.delete()
        return Response({'msg : Data deleted successfully'}, status=status.HTTP_200_OK)



            
