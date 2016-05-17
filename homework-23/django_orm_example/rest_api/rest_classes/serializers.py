# -*- coding: utf-8 -*-

from rest_framework import serializers

from auth_app.models import CustomUser
from pizza.models import PizzaMenuItem

__author__ = 'sobolevn'


class PizzaMenuItemSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class serializing of items from PizzaMenuItem

    Returns:
        List of PizzaMenu field to PizzaMenuItemViewSet (rest_api/rest_classes/views.py)

    """
    class Meta:
        """
        Serializer uses through class Meta model PizzaMenuItem with some fields
        """
        model = PizzaMenuItem
        fields = ('id', 'name')
        """
        """


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class serializing of items from PizzaMenuItem

    Returns:
        List of PizzaMenu field to UserViewSet (rest_api/rest_classes/views.py)

    """
    class Meta:
        """
        Serializer uses through class Meta model CustomUser with some fields

        .. note::
            'favourite_pizza' field uses PizzaMenuItemSerializer to displaying ``id`` of pizza
            ``favourite_pizza = PizzaMenuItemSerializer(required=False)``
        """
        model = CustomUser
        fields = ('id', 'username', 'email', 'our_note', 'favourite_pizza')
        """
        """
    favourite_pizza = PizzaMenuItemSerializer(required=False)

