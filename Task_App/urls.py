
from Task_App import adminviews, userviews
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import urls
from . import views
from . import adminviews
from . import userviews
urlpatterns = [
    path('loginpage', views.loginpage, name="loginpage"),
    path('', views.loginpage, name="loginpage"),
    path('logout_user', views.logout_user,name="logout_user"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('admin_home', adminviews.admin_home, name="admin_home"),
    path('user_home', userviews.user_home, name="user_home"),
    path('createuser', views.createuser, name="createuser"),
    path('createuser_save', views.createuser_save, name="createuser_save"),
    
    url('^', include('django.contrib.auth.urls')),


]