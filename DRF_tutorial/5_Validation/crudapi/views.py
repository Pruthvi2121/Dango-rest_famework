from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.


# Class based views 

@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        stu = Student.objects.all()
        serializer= StudentSerializer(stu , many= True)
        json_data = JSONRenderer().render(serializer.data)

        return HttpResponse(json_data , content_type='application/json' )

    def post(self, request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data is created Successfully '}
            
            json_data = JSONRenderer().render(res)
            
            return HttpResponse(json_data , content_type='application/json' )
        error ={'msg':serializer.errors}
        json_data = JSONRenderer().render(error)
        return HttpResponse( json_data, content_type='application/json' )

    def put(self, request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu, data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Updated Successfully '}

            json_data = JSONRenderer().render(res)
            
            return HttpResponse(json_data , content_type='application/json' )
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type='application/json' )

    def delete(self, request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id= python_data.get('id')
        stu= Student.objects.get(id=id)
        stu.delete()
        res = {'msg':"Data Deleted Successfully"}
        json_data = JSONRenderer().render(res)

        return HttpResponse(json_data, 'application/json')
    
    
        











# Function based Views


# @csrf_exempt
# def StudentAPI(request):

#     if request.method =='GET':
#         stu = Student.objects.all()
#         serializer= StudentSerializer(stu , many= True)
#         json_data = JSONRenderer().render(serializer.data)

#         return HttpResponse(json_data , content_type='application/json' )
    
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data is created Successfully '}
            
#             json_data = JSONRenderer().render(res)
            
#             return HttpResponse(json_data , content_type='application/json' )
#         return HttpResponse({'msg':serializer.errors} , content_type='application/json' )

#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu, data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Updated Successfully '}

#             json_data = JSONRenderer().render(res)
            
#             return HttpResponse(json_data , content_type='application/json' )
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data , content_type='application/json' )

#     if request.method == 'PATCH':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         stu = Student.objects.get(id = id)
#         serializer = StudentSerializer(stu, data=python_data, partial =True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Updated Successfully '}

#             json_data = JSONRenderer().render(res)
            
#             return HttpResponse(json_data , content_type='application/json' )
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data , content_type='application/json' )
    
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id= python_data.get('id')
#         stu= Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg':"Data Deleted Successfully"}
#         json_data = JSONRenderer().render(res)

#         return HttpResponse(json_data, 'application/json')

