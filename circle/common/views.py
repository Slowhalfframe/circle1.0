from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from articles.models import Article
import json

def ArticleList(request):
    '''
    获取文章列表
    :param request:
    :return: 每次返回10个结果
    '''
    pageNow = request.GET.get('pageNow', 1)
    pageSize = request.GET.get('pageSize', 10)
    articles = Article.objects.all().order_by("-create_time")
    try:
        paginator = Paginator(articles, pageSize)
        page = paginator.page(pageNow)
        articleList = []
        for p in page.object_list:
            article = {}
            article['id'] = p.id
            article['title'] = p.title
            article['mark'] = p.content[:33]
            article['cover_img'] = str(p.cover_img)
            article['zan_num'] = p.zan_num
            article['read_num'] = p.count
            article['article_type'] = p.article_type.name
            article['article_typeID'] = p.article_type.id
            articleList.append(article)
            return JsonResponse(articleList, safe=False)
    except Exception as e:
        print(e)
        return HttpResponse(e, status=500)


