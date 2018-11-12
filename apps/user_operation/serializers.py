# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 23:07
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from .models import UserFav
from  rest_framework.validators import UniqueTogetherValidator

class UserFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFav
        fields = ("user", "goods")
        user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )
        # 使用validate方式实现唯一联合
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

