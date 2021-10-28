from rest_framework import viewsets, status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework.views import APIView

from .models import Address, UserList
from .serializer import UserListSerializer, AddressListSerializer

class UsersVievSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('id')
    serializer_class = UserListSerializer

class AddressVievSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressListSerializer

class AddressViev:
    class AddressList(APIView):
        def get(self, request, format=None):
            address = Address.objects.all()
            serializer = AddressListSerializer(address, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = AddressListSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class AddressDetail(APIView):
        def get_object(self,pk):
            try:
                return Address.objects.get(pk=pk)
            except Address.DoesNotExist:
                raise Http404

        def get(self, pk):
            address = self.get_object(pk)

        def put():
            pass
        
        def delete():
            pass

