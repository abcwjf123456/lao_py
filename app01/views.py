from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def test(request):
    return HttpResponse("root")


def test1(request):
    return HttpResponse("ok")


def test2(request, year):
    print(year)
    return HttpResponse("ok")


def test3(request, year):
    print(year)
    return HttpResponse("ok")


def login(request):
    print(request)  # <WSGIRequest: GET '/login/?a=1&b=2'> WSGIRequest类的实例化对象
    print(request.method)
    print(request.POST)
    print(request.GET)  # request.GET.get('a')  == 1
    print(request.path)  # 当前请求路径
    print(request.get_full_path())  # 当前请求路径包含查询参数
    print(request.META)  # 所有请求头的信息 {''HTTP_USER_AGENT':'asdfasdfasdf',....}
    # 	request.META 字典类型数据,所有的请求头的键都加上了一个HTTP_键名称
    return HttpResponse('ok')
def test4(request,year,month):
    print(year)
    print(month)
    return HttpResponse('ok')