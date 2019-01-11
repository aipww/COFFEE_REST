from rest_framework import serializers
from reg.models import UserReg

class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReg
        fields = [
            'pk',
            'user',
            'email',
            'pas',
        ]