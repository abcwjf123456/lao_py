from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def redirect1(request):
    return redirect("http://www.baidu.com")


def redirect_login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        user = request.POST.get('user')
        password = request.POST.get('password')
        print(user, password)
        return HttpResponse("ok")


