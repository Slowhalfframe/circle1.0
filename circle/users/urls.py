from django.conf.urls import url
from users import views
from users.send_email import sendYAZM

urlpatterns = [
    url(r'^sign_in/$', views.SignInView.as_view(), name='sign_in'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^send/$', views.Send, name='send'),
    url(r'^vercode/$', sendYAZM, name='vercode'),
]