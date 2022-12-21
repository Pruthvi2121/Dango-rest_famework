from .models import Song, Singer
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
    # Song = serializers.StringRelatedField(many = True)
    # Song = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    song = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='song-detail')
    song = serializers.SlugRelatedField(many = True, read_only = True, slug_field='title')
    song = serializers.HyperlinkedIdentityField(many= True, view_name='song-detail')
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender','song']


class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']

