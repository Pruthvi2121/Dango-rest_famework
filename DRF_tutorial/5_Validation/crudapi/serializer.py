from .models import Student
from rest_framework import serializers

# Validators
def City_Name_Uppercase(value):
    if value[0].islower():
        raise serializers.ValidationError(" City name should start with Capital Letter") 

    return value


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=255, validators=[City_Name_Uppercase])
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # Field Validation
    def validate_roll(self, value):
        
        if value <= 20:
            raise serializers.ValidationError(" Roll no should greater than 20")

        return value

    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        roll = data.get('roll')
        if nm[0].islower() and roll < 20:
            raise serializers.ValidationError(" Name should Start with Uppercase")
        return data