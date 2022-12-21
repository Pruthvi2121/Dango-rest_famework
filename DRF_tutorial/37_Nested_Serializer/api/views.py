from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import SingerSerializer, SongSerializer

class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
