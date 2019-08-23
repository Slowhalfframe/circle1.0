from django.db import models


class CopyRight(models.Model):
    id = models.AutoField(primary_key=True)
    bah = models.CharField(max_length=33, default='豫ICP备18037195号-1', verbose_name="备案号")
    baLink = models.CharField(max_length=53, default='http://www.miibeian.gov.cn', verbose_name="备案链接")
    title = models.CharField(max_length=66, default='python圈 | (Circle) 专注python相关技术', verbose_name="标题")
    desc = models.CharField(max_length=99, default='科技界的一股清流，情怀程序yuan！', verbose_name="口号")


class FriendLink(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=33, verbose_name="友情链接名称")
    link = models.CharField(max_length=100, verbose_name="友情链接")
    head = models.ImageField(blank=True, null=True, upload_to='static/common/friend/', verbose_name="友链图标")
    sort = models.IntegerField(verbose_name="排序", help_text='数字越大越往前')