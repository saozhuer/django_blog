import re
import time
import logging

from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect, HttpResponse
from user.models import User


class TestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 对所有的请求都进行登陆状态的校验
        # 获取所有请求的连接
        path = request.path
        if path == '/':
            return None
        for p in ['/user/register/', '/user/login/', '/blogweb/index/', '/blogweb/list/',
                  '/blogweb/share/', '/blogweb/about/', '/blogweb/info/',
                  '/blogweb/gbook/', '/blogweb/time/', '/media/.*', ]:
            if re.match(p, path):
                # 跳过以上所有连接 直接访问路由对应的视图函数
                return None
        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            request.user = user
        except Exception as e:
            return HttpResponseRedirect(reverse('user:login'))
