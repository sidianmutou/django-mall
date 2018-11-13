# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 22:40
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from .models import Goods, GoodsCategory, GoodsImage


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        images = GoodsImageSerializer(many=True)
        # fields = ('category', 'goods_sn', 'name', 'click_num', 'sold_num', 'market_price')
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and return a new `Goods` instance, given the validated data.
        """
        return Goods.objects.create(**validated_data)
