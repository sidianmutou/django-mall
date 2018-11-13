from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserRegSerializer,UserDetailSerializer
from rest_framework.generics import mixins
from django.contrib.auth import get_user_model
from utils.permissions import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
User = get_user_model()
# Create your views here.
class CustomBackend(ModelBackend):
    """
    自定义用户验证规则
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因
            # 后期可以添加邮箱验证
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self,
            # raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# 与drf的jwt相关的设置
# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=20),
#     'JWT_AUTH_HEADER_PREFIX': 'JWT',
# }

class UserViewset(mixins.CreateModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    # serializer_class = UserRegSerializer
    # 重写该方法，不管传什么id，都只返回当前用户
    def get_object(self):
        return self.request.user

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []

        return []

    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UserDetailSerializer






