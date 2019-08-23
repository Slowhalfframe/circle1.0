from django.db import models
from django.contrib.auth.models import AbstractUser


class Auth(AbstractUser):
    sex_options = (
        (1, '男'),
        (2, '女'),
    )
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="手机号码")
    sex = models.CharField(choices=sex_options, default=1, max_length=2, verbose_name="性别")
    autograph = models.CharField(max_length=80, blank=True, null=True, verbose_name="个性签名")
    head = models.ImageField(upload_to='static/users/head/', default='static/img/logo.png', verbose_name="用户头像")

    class Meta:
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name


class VerificationCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5, verbose_name="验证码")
    email = models.CharField(max_length=55, verbose_name="邮箱地址")
    # create_time = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name='创建时间')
    create_time = models.CharField(max_length=55, verbose_name="创建时间")