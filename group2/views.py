from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse


# Create your views here.
def kk(request):
    return HttpResponse('ok2')


# 反向解析
def kk2(request):
    return redirect(reverse('kkl'))


def index(request, mobile):
    print(":::", type(mobile))
    return HttpResponse(f"hi,{mobile}用户")
