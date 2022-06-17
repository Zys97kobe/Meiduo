from django.db import models

# Create your models here.
# 1、自己定义模型，密码自己加密和验证
# class User(models.Model):
#     username = models.CharField(max_length=20,unique=True)
#     password = models.CharField(max_length=16)
#     phone = models.CharField(max_length=11,unique=True)

# 2、django自带用户模型，自动进行密码加密和验证
#from django.contrib.auth.models import User

# 继承系统用户模型，然后替换系统用户表。
from django.contrib.auth.models import AbstractUser
class userinfo(AbstractUser):
    phone = models.CharField(max_length=11,unique=True)
    class Meta:
        db_table = '用户信息'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

