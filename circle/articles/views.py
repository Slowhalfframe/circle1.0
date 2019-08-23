from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from users.util import tokenIS
from users.models import Auth
from articles import models
from django.http import QueryDict


def request_body_serialze(request):
    querydict = QueryDict(request.body.decode("utf-8"), encoding="utf-8")
    response_dict = {}
    try:
        for key, val in querydict.items():
            response_dict[key] = val
    except:
        pass
    return response_dict


@tokenIS
def Article(request):
    if request.method.lower() == 'post':
        try:
            title = request.POST['title']
            content = request.POST['content']
            article_from = request.POST['article_from']
            article_type_id = request.POST['article_type']
            articleGroup = request.POST['article_group']
            gropObj = models.ArticleGroup.objects.get(pk=articleGroup)
            cover_img = request.FILES.get('cover_img', 1)
            # print(title, content, article_from, article_type_id, cover_img)
            user = Auth.objects.get(pk=request.user_id)
            articleType = models.ArticleType.objects.get(pk=article_type_id)
            if cover_img == 1:
                article = models.Article(title=title, content=content, article_from=article_from, article_type=articleType, user=user, articleGroup=gropObj)
            else:
                article = models.Article(title=title, content=content, article_from=article_from, article_type=articleType, cover_img=cover_img,  user=user, articleGroup=gropObj)
            article.save()
            return JsonResponse({'articleId': article.id})
        except Exception as e:
            print(e)
            return HttpResponse(status=500)

    if request.method.lower() == 'put':

        pass
    if request.method.lower() == 'delete':
        pass


# 文集操作
@tokenIS
def articleGroup(request):
    if request.method == 'GET':
        user = models.Auth.objects.get(pk=request.user_id)
        group = models.ArticleGroup.objects.filter(user=user)
        artcleGroup = []
        for g in group:
            Groups = {}
            Groups["name"] = g.name
            Groups["id"] = g.id
            artcleGroup.append(Groups)
        data = {'code': 1, 'artcleGroup': artcleGroup}
        return JsonResponse(data)

    if request.method == 'POST':
        name = request.POST['name']
        user = models.Auth.objects.get(pk=request.user_id)
        newGroup = models.ArticleGroup(name=name, user=user)
        newGroup.save()
        return JsonResponse({"group":newGroup.id})

    if request.method == 'PUT':
        # put = request_body_serialze(request)
        # print(put)
        put = QueryDict(request.body)
        print(put)
        # print(put.get(' name'))
        # groupId = put.get('id')
        # name = put.get('name')
        # print(groupId, name)
        # user = models.Auth.objects.get(pk=request.user_id)
        # group = models.ArticleGroup.objects.get(pk=groupId)
        # if group.user == user:
        #     group.name = name
        #     group.save()
        #     return JsonResponse({"group": group.id})
        # else:
        #     return HttpResponse(status=405)