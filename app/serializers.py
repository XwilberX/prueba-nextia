from rest_framework import serializers
from app.models import UserModel, BienesModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username']

class BienesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = BienesModel
        fields = '__all__'