from itsdangerous import TimedJSONWebSignatureSerializer
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from circle import celery
import string
import random
import datetime
from django.http import HttpResponse, JsonResponse

from users.models import VerificationCode


class SendEmail():
    def __init__(self, address):
        # self.user_id = user_id
        self.address = address
        self.ret = True
        self.my_sender = '1441576268@qq.com'
        self.my_pass = 'szlcejiprutxbafa'
        self.SECRET_KEY = 's(do(h$i-d3rzrx7yhw@ik!cgwg+52-c#roc*3gk#wfk2y@1=2'

    def generateToken(self, user_id):
        '''
        生成token
        :return: token
        '''
        ser = TimedJSONWebSignatureSerializer(self.SECRET_KEY, expires_in=3600 * 0.5)
        token = ser.dumps({'confirm': user_id})
        token = token.decode('utf8')
        return token

    def Content(self, emailContent, url, user_id):
        url = url+"/{0}".format(self.generateToken(user_id))
        mail_msg = emailContent + '<br><a href="{0}">点我继续操作</a>'.format(url)
        return mail_msg

    def loginSend(self, msg):
        # 登录
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(self.my_sender, self.my_pass)
        server.sendmail(self.my_sender, [self.address, ], msg.as_string())
        server.quit()
        return self.ret

    def Write(self, mail_msg):
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(["Python圈(Circle)", self.my_sender])
        msg['To'] = formataddr(["尊敬的"+self.address, self.address])
        msg['Subject'] = 'Python圈(Circle)|每个人的笔记家园'
        return msg

    def Start(self, emailContent, url, user_id):
        content = self.Content(emailContent, url, user_id)
        msg = self.Write(content)
        ret = self.loginSend(msg)
        print(ret)

    def yzm(self):
        # 1. 生成四位验证码
        randomNum = self.getRandomChar()
        # 2. 持久化存储
        print(randomNum, '/', self.address)
        # issave = VerificationCode.objects.get(email=self.address)
        # if issave:
        #     obj = VerificationCode(email=self.address, code=randomNum)
        # obj.save()
        VerificationCode.objects.update_or_create(email=self.address, defaults={'code': randomNum.upper(), 'create_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        # 3. 发送
        mail_msg = '您的注册验证码为:{0}! 30分钟内有效！！'.format(randomNum)
        msg = self.Write(mail_msg)
        ret = self.loginSend(msg)
        print(ret)
        return randomNum

    # 获取一个随机字符串，4位的
    def getRandomChar(self, count=4):
        # 生成随机字符串
        # string模块包含各种字符串，一下位小写字母加数字
        ran = string.ascii_lowercase + string.ascii_uppercase + string.digits
        char = ''
        for i in range(count):
            char += random.choice(ran)
        return char


# s = SendEmail('zhanghaoran@qidufanyi.com', 1)
# s.Start('<h1>Welcome!!! </h1>', 'http://www.baidu.com')

@celery.app.task
def send(address, user_id, url):
    '''
    序列化邮箱ID 发送到收件人邮箱 用户点击生成的唯一ID 生成的URL  点击认证
    :param address: 收件人邮箱
    :param user_id: 用户 ID  会序列化
    :param url: 用户认证 地址
    :return: 发送邮箱
    '''
    print(address)
    s = SendEmail(address)
    s.Start('<h1>Welcome!!! </h1>', url, user_id)


def sendYAZM(request):
    address = request.GET.get('address', '')
    # print(address)
    if address != '':
        try:
            s = SendEmail(address)
            code = s.yzm()
            return JsonResponse({'code': code}, status=200)
        except Exception as e:
            print(e)
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)