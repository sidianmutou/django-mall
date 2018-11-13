# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 23:14
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : signals.py
# @Software: PyCharm

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import UserProfile
from django.contrib.auth import get_user_model
User = get_user_model()


# 参数一接收哪种信号，参数二是接收哪个model的信号
@receiver(post_save, sender=UserProfile)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    # 是否新建，因为update的时候也会进行post_save
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()
