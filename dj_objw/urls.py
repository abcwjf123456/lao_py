"""dj_objw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from app01 import views

# from group2 import views

urlpatterns = [

    re_path('^$', views.test),
    path('admin/', admin.site.urls),
    path('django3/', views.test1),
    path('django4/<int:year>/', views.test2),
    # 无名分组
    re_path('django5/(\d+)/', views.test3),
    re_path('django6/', views.login),
    # 有名分组
    re_path('django7/(?P<year>\d+)/(?P<month>\d+)/', views.test4),
    # 老男孩2.0 django基础开发路由_orm内容代码练习
    path('group2/', include('group2.urls')),

]
