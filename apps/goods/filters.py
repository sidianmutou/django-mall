# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 17:27
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : filters..py
# @Software: PyCharm


from django_filters import rest_framework as filters
from .models import Goods
from django.db.models import Q

class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    # 指定字段以及字段上的行为，在shop_price上大于等于
    price_min = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    # 行为: 名称中包含某字符，且字符不区分大小写
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name','is_hot','is_new']

    top_category = filters.NumberFilter(field_name="category", method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        # 不管当前点击的是一级目录二级目录还是三级目录。
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

