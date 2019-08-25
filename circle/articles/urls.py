from django.conf.urls import url
from articles import views

urlpatterns = [
    url(r'^detail/<\d+>/?$', views.ArticleDetai.as_view(), name='detail'),
    url(r'^article/$', views.Article, name='article'),
    url(r'^group/$', views.articleGroup, name='group'),
]