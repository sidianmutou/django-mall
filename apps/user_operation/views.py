from django.shortcuts import render

# Create your views here.
from rest_framework.generics import mixins
from rest_framework import viewsets
from .models import UserFav, UserLeavingMessage, UserAddress
from .serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer, AddressSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly


class UserFavViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    """
    用户收藏功能
    """

    # queryset = UserFav.objects.all()
    # 设置动态的Serializer
    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer

    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    lookup_field = 'goods_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)


class LeavingMessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言功能
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LeavingMessageSerializer

    # 只能看到自己的留言
    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class AddressViewset(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
