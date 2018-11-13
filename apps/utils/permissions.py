# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 00:50
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : permissions.py
# @Software: PyCharm


from rest_framework import permissions
# from users.models import UserProfile

# user =UserProfile
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user




