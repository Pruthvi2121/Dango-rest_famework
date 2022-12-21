from .models import *
from rest_framework.serializers import ModelSerializer


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration']

class SingerSerializer(ModelSerializer):
    song_detail = SongSerializer(many = True, read_only = True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song_detail']

