from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.urls import reverse

from user.models import Category, User, Article


def index(request):
    if request.method == 'GET':
        # 获取数据库文章
        arts = Article.objects.all()[::-1]
        g_art = [[i, arts[i]] for i in range(len(arts))]
        for i in g_art:
            i[0] = 1 if i[0] & 1 else 2
        return render(request, 'web/index.html', {'g_art': g_art,'arts':arts})


def share(request):
    if request.method == 'GET':
        return render(request, 'web/share.html')


def list(request):
    if request.method == 'GET':
        # 获取数据库文章
        arts = Article.objects.all()

        return render(request, 'web/list.html', {'arts': arts})


def about(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')


def gbook(request):
    if request.method == 'GET':
        return render(request, 'web/gbook.html')


def time(request):
    if request.method == 'GET':
        #获取数据库时间的文章对象
        arts = Article.objects.all()[::-1]

        return render(request, 'web/time.html',{'arts':arts})


def info(request):
    if request.method == 'GET':
        # 获取点击的文章id
        id = request.GET.get('id')
        # 获取id对应的数据库文章对象
        art = Article.objects.filter(pk=id).first()
        return render(request, 'web/info.html', {'art': art})
