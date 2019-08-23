from django.contrib import admin
from django.utils.safestring import mark_safe
from articles import models


@admin.register(models.ArticleType)
class ArticleType(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_cover', 'parent')
    list_per_page = 10
    ordering = ('id', )
    list_editable = []
    list_display_links = ('name', )
    list_filter = ('create_time', )  # 过滤器
    search_fields = ('name', )  # 搜索字段

    def type_cover(self, obj):
        return mark_safe('<img src="/%s" width="30px" />' % obj.cover)


@admin.register(models.ArticleGroup)
class ArticleGroup(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'sort')
    list_per_page = 10
    ordering = ('sort', )
    list_editable = ['status', 'sort']
    list_display_links = ('name', )
    list_filter = ('status', 'create_time')  # 过滤器
    search_fields = ('name', )  # 搜索字段


@admin.register(models.Article)
class Article(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'articleGroup')
    list_per_page = 10
    ordering = ('id', )
    list_editable = []
    list_display_links = ('title', )
    list_filter = ('create_time', )  # 过滤器
    search_fields = ('title', )  # 搜索字段


@admin.register(models.Comments)
class Comments(admin.ModelAdmin):
    list_display = ('id', 'article', 'content', 'user', 'parentCom')
    list_per_page = 10
    ordering = ('id', )
    list_editable = []
    list_display_links = ('article', )
    list_filter = ('create_time', )  # 过滤器
    search_fields = ('article', )  # 搜索字段


@admin.register(models.Article_zan_log)
class Article_zan_log(admin.ModelAdmin):
    list_display = ('id', 'link_user', 'link_article', 'status')
    list_per_page = 10
    ordering = ('id', )
    list_editable = []
    list_display_links = ('link_user', 'link_article')
    list_filter = ('status', )  # 过滤器
    search_fields = ('link_article', )  # 搜索字段


@admin.register(models.Article_count)
class Article_count(admin.ModelAdmin):
    list_display = ('id', 'link_user', 'link_article', 'status')
    list_per_page = 10
    ordering = ('id', )
    list_editable = []
    list_display_links = ('link_user', 'link_article')
    list_filter = ('status', )  # 过滤器
    search_fields = ('link_article', )  # 搜索字段


@admin.register(models.Favorites)
class Favorites(admin.ModelAdmin):
    list_display = ('id', 'favorites_articles', 'user', 'status')
    list_per_page = 10
    ordering = ('id', )
    list_editable = []
    list_display_links = ('user', 'favorites_articles')
    list_filter = ('status', )  # 过滤器
    search_fields = ('favorites_articles', )  # 搜索字段
