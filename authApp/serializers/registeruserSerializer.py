from authApp.models import register_user
from authApp.models.register_user import Register_user
from rest_framework import serializers

class RegisteruserSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Register_user
        fields = ['user_id', 'name', 'last_name', 'nickname', 'password', 'email', 'adress', 'cellphone']

def create(self, validated_data):
    registeruserInstance = Register_user.objects.create(**validated_data)
    return registeruserInstance