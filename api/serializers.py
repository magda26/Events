from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.models import TokenModel
from .models import Event


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password2 = None

    def custom_signup(self, request,user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name','last_name'])

    def validate(self, data):
        return data

class CustomTokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source ='key')
    class Meta:
        model = TokenModel
        fields = ('token',)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('user','creation_date')
