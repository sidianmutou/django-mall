# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 22:39
# @Author  : Olex
# @Email   : olex1216@gmail.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕课小店"
    site_footer = "olex1216"
    # menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

