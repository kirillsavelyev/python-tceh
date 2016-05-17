# -*- coding: utf-8 -*-

from rest_framework import viewsets

from pizza.models import PizzaMenuItem
from auth_app.models import CustomUser
from rest_api.rest_classes.serializers import (
    PizzaMenuItemSerializer,
    UserSerializer,
)

__author__ = 'sobolevn'


class PizzaMenuItemViewSet(viewsets.ModelViewSet):
    """
    This class that create ViewSet of PizzaMenuItem
    Registered in the urls by using a router API (rest_api/urls.py)

    Returns:
        View of PizzaMenu fields from PizzaMenuItemSerializer (rest_api/rest_classes/serializers.py)

    All Pizza items serialized by PizzaMenuItemSerializer

    ``queryset = PizzaMenuItem.objects.all()``

    ``serializer_class = PizzaMenuItemSerializer``
    """

    queryset = PizzaMenuItem.objects.all()
    """
    """
    serializer_class = PizzaMenuItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This class that create ViewSet of Users
    Registered in the urls by using a router API (rest_api/urls.py)

    Returns:
        View of User fields from UserSerializer (rest_api/rest_classes/serializers.py)

    All User items serialized by UserSerializer

    ``queryset = CustomUser.objects.all()``

    *serializer_class = UserSerializer
    """
    queryset = CustomUser.objects.all()
    """
    """
    serializer_class = UserSerializer
