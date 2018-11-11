# -*- coding: utf-8 -*-
# @Time    : 2018/11/7 22:12
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : view_base.py
# @Software: PyCharm

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import Goods
from .serializers import GoodsSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

class GoodsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        商品列表页
        """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


    # def post(self, request, format=None):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



