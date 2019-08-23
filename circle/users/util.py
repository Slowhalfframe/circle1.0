from itsdangerous import TimedJSONWebSignatureSerializer as tjs
from django.http import JsonResponse, HttpResponse
import re


secretKey = '&-lxnstds02q!gt)xtnu%n4g#dp3mptb7ree^5bcp72pq2(5-('
s = tjs(secretKey, expires_in=60*60*5)


def deToken(id):
    '''
    :param id: 用户ID
    :return: 加密后的token
    '''
    token = s.dumps({'user_id': id}).decode('utf8')
    return token


def enToken(token):
    '''
    :param token: 请求头中的token
    :return: 未过期：用户ID  过期：False
    '''
    try:
        data = s.loads(token)
        user_id = data['user_id']
        return user_id
    except:
        return False


# 验证token
# 不可用于类中
def tokenIS(func):
    def _checkToken(request):
        # try:
        token = request.META.get('HTTP_TOKEN')
        res = enToken(token)
        if res:
            request.user_id = res
            return func(request)
        else:
            return HttpResponse(status=403)
        # except:
        #     return HttpResponse(status=403)
    return _checkToken


def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False