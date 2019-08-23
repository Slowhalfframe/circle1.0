from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import datetime

from users.models import Auth, VerificationCode
from users import util
from users import send_email


# 重写认证方法
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Auth.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
            if user.check_password(password):
                return user
        except:
            return None


class SignInView(APIView):
    def get(self, request):
        '''
        验证token可用性， 并返回用户信息
        :param request: header -- token
        :return: username, head, id / 错误状态码: 403
        '''
        # 获取token
        token = request.META.get('HTTP_TOKEN')
        if token != None:
            user_id = util.enToken(token)
            if user_id:
                user = Auth.objects.get(pk=user_id)
                return Response({'code': 1, 'data': {'user_id': user.id, 'user_name': user.username, 'user_head': str(user.head)}})
            else:
                # token 过期
                return Response(status=403)
        else:
            # 不存在token
            return Response(status=403)

    # @util.tokenIS()
    def post(self, request):
        '''
        用户登陆
        :param request: username  password
        :return: id, username, head, token  /  401
        '''
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        authentication = CustomBackend()
        user = authentication.authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                token = util.deToken(user.id)
                return Response({'code': 1, 'data': {'user_id': user.id, 'user_name': user.username, 'user_head': str(user.head), 'token': token}})
            else:
                return Response({'status': 401.4})
        else:
            return Response({'status': 401.1})


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        code = request.POST['code']
        if util.validateEmail(email):
            # 验证邮箱有效性
            codeObj = VerificationCode.objects.get(code=code, email=email)
            if codeObj:
                # 判断是否过期
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if (datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(codeObj.create_time, '%Y-%m-%d %H:%M:%S')).seconds <= 1800:
                    if len(password) >= 6:
                        user = Auth(email=email, username=email, is_staff=1)
                        user.set_password(password)
                        user.save()
                        token = util.deToken(user.id)
                        return Response({'code': 1, 'data': {'user_id': user.id, 'user_name': user.username, 'user_head': str(user.head), 'token': token}})
                    else:
                        return Response({'code': -4, 'error_msg': '密码长度不够'})
                else:
                    return Response({'code': -4, 'error_msg': '验证码已过期'})
            else:
                return Response({'code': -4, 'error_msg': '验证码不正确'})
        else:
            return Response({'code': -4, 'error_msg': '邮箱长度不够或格式不正确'})


def Send(request):
    print("开始发送")
    send_email.send.delay('18569938068@163.com', 'abcd')
    return JsonResponse({'msg': '发送完成'})