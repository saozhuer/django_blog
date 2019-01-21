
from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns =[

    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('article/',views.article,name='article'),
    path('category/',views.category,name='category'),
    path('add-article/',views.add_article,name='add-article'),
    path('logout/',views.logout,name='logout'),
    path('del_art/',views.del_art,name='del_art'),
    path('update_article/',views.update_article,name='update-article'),
    # 编辑文章
    path(r'edit_article/', views.edit_article, name='edit_article'),
    #删除栏目
    path('del_cate/',views.del_cate,name='del_cate'),
    #修改文章
    path('update_cate/',views.update_cate,name='update_cate'),



]

