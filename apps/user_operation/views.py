from django.shortcuts import render

# Create your views here.
from rest_framework.generics import mixins
from rest_framework import viewsets
from .models import UserFav
from .serializers import UserFavSerializer

class UserFavViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    """
    用户收藏功能
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer