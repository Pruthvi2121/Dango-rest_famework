from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def CreateStudent(request):
    if request.method == 'POST':
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data is created Successfully '}
            json_data = JSONRenderer().render(res)
            
            return HttpResponse(json_data, content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type= 'application/json')