# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from rest_framework import routers

from rest_api.rest_classes.views import UserViewSet, PizzaMenuItemViewSet

__author__ = 'sobolevn'

router = routers.DefaultRouter()
"""
Registering URL of ViewSet

:param PartOfUrl  Url name: ``r'users'`` displayed in the address bar.

:param ViewClassName ViewSet:  Import from rest_classes/views.py

Create router instance and register view sets

``router.register(r'users', UserViewSet)``

``router.register(r'pizzamenuitem', PizzaMenuItemViewSet)``

"""

router.register(r'users', UserViewSet)
router.register(r'pizzamenuitem', PizzaMenuItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
"""
Result of registering urls

    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept\n
    {
        "users": "http://127.0.0.1:8000/api/users/",\n
        "pizzamenuitem": "http://127.0.0.1:8000/api/pizzamenuitem/"
    }
"""