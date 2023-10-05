from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json


# Create your views here.
@csrf_exempt
def index(request):
    print(request.method)
    # POST
    # print(request.body)
    # print(request.POST)
    # user=request.POST.get('user')
    # print(user)
    # print(request.POST.get('pwd'))
    # print(request.POST.getlist('pwd'))
    # b'user=yuan&pwd=123&pwd=129'
    # <QueryDict: {'user': ['yuan'], 'pwd': ['123', '129']}>
    # yuan
    # 129
    # ['123', '129']

    # GET
    print(request.GET)
    print(request.GET.get("user"))
    print(request.META)
    print(request.META.get("SERVER_PORT"))
    print(request.path)
    # print(request.get_full_path())
    return HttpResponse('ok')


def index1(request):
    res = {"hh": "哈哈", "f": 12}
    res1 = [{"hh": "哈哈", "f": 12}]
    # return HttpResponse(json.dumps(res, ensure_ascii=False),content_type='application/json')  # ensure_ascii=False 让返回值成中文
    # JsonResponse做了两步第一步:序列化字典 第二步:content_type='application/json'将字符格式解成json格式
    # JsonResponse没办法序列化字典以外格式,其它格式需要加safe=Flase
    return JsonResponse(res1, safe=False)
