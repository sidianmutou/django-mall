# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 22:12
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : view_base.py
# @Software: PyCharm

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter

class GoodsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
        商品列表页
        """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')

    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter

    # 设置我们的search字段
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 设置排序
    ordering_fields = ('sold_num', 'add_time')



    # def get_queryset(self):
    #     # 价格大于100的
    #     price_min = self.request.query_params.get('price_min', 0)
    #     if price_min:
    #         self.queryset = Goods.objects.filter(shop_price=price_min).order_by('-add_time')
    #     return self.queryset

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, format=None):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer

