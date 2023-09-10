from django.shortcuts import render,HttpResponse

# Create your views here.
def kk(request):
    return HttpResponse('ok2')

def index(request,mobile):
    print(":::",type(mobile))
    return HttpResponse(f"hi,{mobile}用户")