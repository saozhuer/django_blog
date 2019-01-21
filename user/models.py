from django.db import models

# Create your models here.

#创建一个用户的表格



class User(models.Model):
    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=150,null=False)
    crate_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class Category(models.Model):
    c_name = models.CharField(max_length=10)
    f_id = models.ForeignKey('self',related_name='father',on_delete=models.CASCADE) #父ID

    class Meta:
        db_table = 'category'


class Article(models.Model):
    title = models.CharField(max_length=15,unique=True,null=True)
    content = models.TextField(null=False)
    keyword = models.CharField(max_length=8,null=True)
    description = models.CharField(max_length=25,null=True)
    icon = models.ImageField(upload_to='upload',null=True)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)
    f = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,related_name='category')
    class Meta:
        db_table = 'article'



