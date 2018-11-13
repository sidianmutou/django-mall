from django.shortcuts import render

# Create your views here.
from rest_framework.generics import mixins
from rest_framework import viewsets
from .models import UserFav
from .serializers import UserFavSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated
# from utils.permissions import IsOwnerOrReadOnly

class UserFavViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    """
    用户收藏功能
    """
    # queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)
