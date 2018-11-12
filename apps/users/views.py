from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from rest_framework import viewsets
# from .models import UserProfile
from .serializers import UserRegSerializer
from rest_framework.generics import mixins
from django.contrib.auth import get_user_model
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

class UserViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer