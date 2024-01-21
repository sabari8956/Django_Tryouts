from rest_framework import serializers
from .models import profile, User

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'

class USerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"