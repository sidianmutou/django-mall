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
from goods.serializers import GoodsSerializer
from rest_framework.response import Response
class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        from django.forms.models import model_to_dict
        for good in goods:
            json_dict = model_to_dict(good)
            json_list.append(json_dict)

        import json
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        return JsonResponse(json_data, safe=False)

    def post(self, request, format=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



