from django.conf.urls import url ,include
from django.contrib import admin
from neha import views


urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^$', views.header, name='header'),
    url(r'^login/$',views.login ,name="login"),
    url(r'^login/afterlogin/$',views.afterlogin ,name="afterlogin"),
    url(r'^login/error/$', views.afterlogin, name="error"),

]