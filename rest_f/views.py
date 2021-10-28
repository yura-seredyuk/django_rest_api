from rest_framework import viewsets


from .models import Address, UserList
from .serializer import UserListSerializer, AddressListSerializer

class UsersVievSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('id')
    serializer_class = UserListSerializer

class AddressVievSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressListSerializer