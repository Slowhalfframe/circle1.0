from django.db import models
from mdeditor.fields import MDTextField

from users.models import Auth


class ArticleType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True, verbose_name="文章类别名称")
    cover = models.ImageField(upload_to='static/articles/type_cover', default="static/img/logo.png", verbose_name="文章分类图像")
    intro = models.TextField(verbose_name="文章类别描述")
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name="父级类型", on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):  # ____unicode____ on Python 2
        return self.name

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name


class ArticleGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=56, verbose_name="文集名称")
    user = models.ForeignKey(Auth, on_delete=models.CASCADE, verbose_name="文集创建者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    status = models.BooleanField(default=True, verbose_name="文集状态")
    sort = models.IntegerField(default=0, verbose_name="文集排序")

    class Meta:
        verbose_name = '文集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    FROM_CHOICES = (
        ('1', '原创'),
        ('2', '转载'),
        ('3', '翻译'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=223, verbose_name="文章标题")
    content = MDTextField(verbose_name="文章内容")
    cover_img = models.ImageField(null=True, blank=True, upload_to="static/articles/cover", verbose_name="文章封面图")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    change_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    article_from = models.CharField(max_length=16, choices=FROM_CHOICES, verbose_name="文章来源")
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name="文章分类")
    count = models.IntegerField(default=0, verbose_name="阅读量")
    zan_num = models.IntegerField(default=0, verbose_name="点赞量")
    # comment = models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name="评论")
    user = models.ForeignKey(Auth, on_delete=models.CASCADE, verbose_name="关联用户")
    articleGroup = models.ForeignKey(ArticleGroup, on_delete=models.CASCADE, verbose_name="关联文集")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章列表'
        verbose_name_plural = verbose_name


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="关联文章")
    content = models.TextField(verbose_name="评论内容")
    # content = MDTextField
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    user = models.ForeignKey(Auth, on_delete=models.CASCADE, verbose_name="关联用户")
    # 评论自关联 为评论的回复1
    parentCom = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name="评论自关联父级")

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name


class Article_zan_log(models.Model):
    id = models.AutoField(primary_key=True)
    link_user = models.ForeignKey(Auth, on_delete=models.CASCADE, verbose_name="关联用户")
    link_article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="关联文章")
    status = models.BooleanField(verbose_name="状态", default=1)

    def __str__(self):
        return '{0}点赞了文章：{1}'.format(self.link_user, self.link_article)

    class Meta:
        verbose_name = '文章点赞记录'
        verbose_name_plural = verbose_name


class Article_count(models.Model):
    id = models.AutoField(primary_key=True)
    link_user = models.ForeignKey(Auth, on_delete=models.CASCADE, verbose_name="关联用户")
    link_article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="关联文章")
    status = models.BooleanField(verbose_name="状态", default=1)

    def __str__(self):
        return '{0}浏览了文章：{1}'.format(self.link_user, self.link_article)

    class Meta:
        verbose_name = '文章浏览记录'
        verbose_name_plural = verbose_name


class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Auth, on_delete=models.CASCADE)
    favorites_articles = models.ForeignKey(Article, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(verbose_name="状态", default=1)

    def __str__(self):
        return '{0}收藏了文章：{1}'.format(self.user, self.favorites_articles)

    class Meta:
        verbose_name = '文章收藏记录'
        verbose_name_plural = verbose_name