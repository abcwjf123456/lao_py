from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def group_one(request):
    name = "root"
    age = 13
    sex = True
    books = ("gg", "kk")
    books2 = ()
    lve = ["swimming", "shopping", "coding", "game"]
    book_info = {"id": 1, "price": 9.90, "name": "python3天入门到挣扎", }
    book_list = [
        {"id": 10, "price": 9.90, "name": "python3天入门到挣扎", },
        {"id": 11, "price": 19.90, "name": "python7天入门到垂死挣扎", },
    ]
    tel = "12345678901"
    import datetime
    data = datetime.datetime.now()
    return render(request, "index.html", locals())


def group_two(request):
    return render(request, 'order.html')


def group_tree(request):
    return render(request, 'base.html')
