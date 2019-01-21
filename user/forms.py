from django import forms

#校验页面中的username和userpwd字段
from user.models import User

class UserForm(forms.Form):
    username = forms.CharField(max_length=10,
                               min_length=2,
                               required=True,# 表示username是必填值
                               error_messages={
                                   'required':'用户名必填',
                                   'min_length':'用户名不能少于2个字符',
                                    'max_length':'用户名不能超过10个字符',
                               }
                               )
    userpwd = forms.CharField(max_length=18,
                              min_length=6,
                              required=True,
                              error_messages={
                                  'required': '密码必填',
                                  'min_length': '密码不能少于6个字符',
                                  'max_length': '密码不能超过18个字符',
                              }
                              )
    userpwd1 = forms.CharField(max_length=18,
                              min_length=6,
                              required=True,
                              error_messages={
                                  'required': '密码必填',
                                  'min_length': '密码不能少于6个字符',
                                  'max_length': '密码不能超过18个字符',
                              }
                              )