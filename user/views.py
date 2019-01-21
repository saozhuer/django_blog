from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect,JsonResponse
# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from user.models import User, Article, Category


#登录
def login(request):
    if request.method == 'GET':
        return render(request,'back/login.html')

    if request.method == 'POST':
        #获取页面数据
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        #获取数据库username对应的信息
        user = User.objects.filter(username=username).first()
        #判断账号密码是否正确
        if check_password(password,user.password):
            # 1.向cookies中保存键值对，键为session_id
            # 2.向django_session表中存session_id值
            # 3.向django_session表中存储键值对{‘username’：saozhuer}
            # request.session['username'] = username
            request.session['user_id']=user.id
            return HttpResponseRedirect(reverse('user:index'))
        else:
            msg = '账号密码错误,请重新登录'
            return render(request,'back/login.html',{'msg':msg})


#首页
def index(request):
    if request.method =='GET':
        return render(request,'back/index.html')


#注册
def register(request):
    if request.method == 'GET':
        return render(request,'back/register.html')
    if request.method == 'POST':
        # 1.接收页面中传递的参数
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        password1 = request.POST.get('userpwd1')
        # 2.实现保存用户信息到user表中
        if User.objects.filter(username=username).exists():
            msg = '账号已存在'
            return render(request,'back/register.html',{'msg':msg})
        if password != password1:
            msg = '密码不一致'
            return render(request,'back/register.html',{'msg':msg})
        password = make_password(password)  # make_password将密码进行加密编码
        User.objects.create(username=username,password=password)
        return HttpResponseRedirect(reverse('user:login'))

#文章页面
def article(request):
    if request.method =='GET':
        #获取文章对象
        # 获取分页的角码
        page = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        # 获取文章数量
        art_num = len(articles)
        # 分页
        pg = Paginator(articles, 3)
        articles = pg.page(page)


        return render(request,'back/article.html',{'articles': articles,'art_num':art_num})
    if request.method == 'POST':
        pass

#栏目页面
@csrf_exempt
def category(request):
    if request.method == 'GET':
        #获取所有栏目
        cates = Category.objects.all()
        #栏目总数
        len_cates = len(cates)

        return render(request,'back/category.html',{'cates':cates,'len_cates':len_cates})
    if request.method == 'POST':
        name = request.POST.get('name')
        fid = request.POST.get('fid')
        Category.objects.create(c_name=name,f_id_id=fid)
        return HttpResponseRedirect(reverse('user:category'))




#添加文章
def add_article(request):
    if request.method =='GET':
        #获取栏目
        cates = Category.objects.all()

        return render(request,'back/add-article.html',{'cates':cates})
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        icon = request.FILES.get('titlepic')
        f_id = request.POST.get('category')


        Article.objects.create(title=title,
                               content=content,
                               keyword=keywords,
                               description=describe,
                               icon=icon,
                               f_id=f_id
                               )
        return HttpResponseRedirect(reverse('user:article'))




def edit_article(request):
    """
    文章编辑方法
    """
    if request.method == 'GET':
        return render(request, 'edit.html')
    if request.method == 'POST':
        # 获取文章的标题和内容
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 使用all()方法进行判断，如果文章标题和内容任何一个参数没有填写，则返回错误信息
        if not all([title, content]):
            msg = '请填写完整的参数'
            return render(request, 'edit.html', {'msg': msg})
        # 创建文章
        Article.objects.create(title=title,
                               content=content)
        # 创建文章成功后，跳转到文章列表页面
        return HttpResponseRedirect(reverse('users:article'))

#退出登录
def logout(request):
    if request.method == 'GET':
        request.session.flush()
        return HttpResponseRedirect(reverse('user:login'))

#删除文章
@csrf_exempt
def del_art(request):

    if request.method =='GET':
        id = request.GET.get('id')
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('user:article'))


#修改文章
@csrf_exempt
def update_article(request):  #<WSGIRequest: GET '/user/update_article/?id=12'>
    if request.method =='GET':
        id = request.GET.get('id')
        articles = Article.objects.filter(pk=id).first()  #Article object (12)
        # 获取栏目
        cates = Category.objects.all()
        return render(request,'back/update-article.html',{'articles':articles,'cates':cates})
#update-article.html
    if request.method =='POST':
        #获取页面上的数据
        web_title = request.POST.get('title')
        web_content = request.POST.get('content')
        web_keywords = request.POST.get('keywords')
        web_describe = request.POST.get('describe')
        web_icon = request.FILES.get('titlepic')
        web_cate = request.POST.get('category')
        #将页面上的数据修改到数据库中
        id = request.GET.get('id')
        article = Article.objects.filter(pk=id).first()

        article.title=web_title
        article.content=web_content
        article.keyword = web_keywords
        article.description = web_describe
        article.icon = web_icon
        article.f_id=web_cate
        article.save()
        # Article.objects.filter(pk=id).update(
        #     title=web_title,
        #     content=web_content,
        #     keyword = web_keywords,
        #     description = web_describe,
        #     icon = web_icon,
        #     f_id=web_cate
        # )
        return HttpResponseRedirect(reverse('user:article'))



#删除栏目
@csrf_exempt
def del_cate(request):
    if request.method == 'GET':

        return HttpResponseRedirect(reverse('user:category'))
    if request.method =='POST':
        id= request.POST.get('id')
        cate = Category.objects.filter(pk=id)
        Category.objects.filter(pk=id).delete()

        return HttpResponseRedirect(reverse('user:category'))



#修改栏目
@csrf_exempt
def update_cate(request):
    if request.method=='GET':
        #从数据库获取栏目
        id = request.GET.get('id')
        cate = Category.objects.filter(pk=id).first()
        cates = Category.objects.all()

        return render(request,'back/update-category.html',{'cate':cate,'cates':cates})

    if request.method =='POST':
        #获取页面上的数据
        name = request.POST.get('name')
        fid = request.POST.get('fid')

        #将页面上的数据更新到数据库
        id = request.GET.get('id')
        Category.objects.filter(pk=id).update(c_name=name,f_id=fid)
        return HttpResponseRedirect(reverse('user:category'))
