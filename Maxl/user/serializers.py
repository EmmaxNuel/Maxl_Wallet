from rest_framework import serializers

from wallet.models import Wallet
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password','phone']

        extra_kwargs = {
            'password': {'write_only': True},
        }


