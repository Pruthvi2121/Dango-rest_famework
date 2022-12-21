from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from  rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.


def Student_detail(request, pk):
    obj = Student.objects.get(id = pk)
    serilizer = StudentSerializer(obj)
    json_data = JSONRenderer().render(serilizer.data)

    return HttpResponse(json_data, content_type ='application/json')

def Student_details(request):
    obj = Student.objects.all()
    serilizer = StudentSerializer(obj, many= True )
    json_data = JSONRenderer().render(serilizer.data)

    return HttpResponse(json_data, content_type ='application/json')

