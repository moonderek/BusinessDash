from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

#View serializre object representation
'''
from myapp.serializers import AccountSerializer
serializer = AccountSerializer()
print(repr(serializer))
'''

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

#Register Serializer 
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'] )
        return user

    def validate_email(self,validated_data):
        if 'email' not in validated_data:
            error_messages = {"email": ["Must include email"]}
            raise serializers.ValidationError(error_messages)
        return validated_data

#Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        #built in auth
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

