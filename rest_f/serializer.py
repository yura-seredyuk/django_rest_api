from rest_framework import serializers
from .models import UserList, Address


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'country', 'city', 'zip_code', 'street', 'house_num', 'apartaments']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']