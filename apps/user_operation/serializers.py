# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 23:07
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from .models import UserFav,UserLeavingMessage,UserAddress
from rest_framework.validators import UniqueTogetherValidator
from goods.serializers import GoodsSerializer


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

class UserFavDetailSerializer(serializers.ModelSerializer):

    # 通过goods_id拿到商品信息。就需要嵌套的Serializer
    goods = GoodsSerializer()
    class Meta:
        model = UserFav
        fields = ("goods", "id")

        class LeavingMessageSerializer(serializers.ModelSerializer):
            user = serializers.HiddenField(
                default=serializers.CurrentUserDefault()
            )
            add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

            class Meta:
                model = UserLeavingMessage
                fields = ("user", "message_type", "subject", "message", "file", "id", "add_time")



class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    class Meta:
        model = UserLeavingMessage
        fields = ("user", "message_type", "subject", "message", "file", "id" ,"add_time")



class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "address", "signer_name", "add_time", "signer_mobile")


