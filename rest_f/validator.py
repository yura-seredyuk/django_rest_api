from rest_framework.utils.representation import smart_repr
from rest_framework import serializers
import re


class AddressValidator:
    message="Validation error: "
    def __init__(self, message=None):
        self.validated_field = ''
        self.validated_data = None
        self.message = message or self.message

    def __call__(self, attrs):
        message = self.message
        if 'apartaments'in attrs and attrs['apartaments'] <= 0:
            message = 'cannot be less than zero'
            self.raize_error(attrs, 'apartaments', message)
            # 'city':
            # 'country': 
            # 'house_num': 
            # 'street': 
            # 'zip_code':
    def raize_error(self, attrs, field_name, message):
        message = self.message + f'The {field_name} field {message}.'
        self.validated_field = field_name
        self.validated_data = attrs[field_name]
        raise serializers.ValidationError(message, code=field_name)

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.validated_field}={self.validated_data})>'
    