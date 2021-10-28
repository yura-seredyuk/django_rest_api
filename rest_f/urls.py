from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users-list', views.UsersVievSet)
router.register(r'address-list', views.AddressVievSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('address/', views.AddressViev.AddressList.as_view())
]