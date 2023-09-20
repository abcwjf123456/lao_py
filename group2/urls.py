from django.urls import path, re_path, include, register_converter
from group2 import views


# 自定义路由转换器
class MobileConverter(object):
    regex = "1[3-9]\d{9}"

    def to_python(self, value):
        print(type(value))
        print(value)
        # 将匹配结果传递到视图内部时使用
        # 返回str还是int主要看需求,纯数字的可以返回int
        return str(value)

    def to_url(self, value):
        # 将匹配结果用于反向解析传值时使用
        return value


# register_converter(路由转换器的类名,调用别名)
register_converter(MobileConverter, "mobile")

urlpatterns = [
    # 测试路由分发代码
    path('kk/', views.kk, name='kkl'),

    # 反向解析
    path('kk2/', views.kk2),

    #  自定义路由正则
    path("index/<mobile:mobile>", views.index)
]
