from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , RetrieveModelMixin, CreateModelMixin , UpdateModelMixin , DestroyModelMixin

class StudentList(GenericAPIView, ListModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class StudentCreate(GenericAPIView, CreateModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentUpdate(GenericAPIView, UpdateModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class StudentDestroy(GenericAPIView, DestroyModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
