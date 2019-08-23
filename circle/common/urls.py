from django.conf.urls import url
from common import views

urlpatterns = [
    url(r'loadArticle', views.ArticleList, name='ArticleList'),
]