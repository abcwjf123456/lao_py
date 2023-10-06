from django.urls import path, re_path, include
from group5.views import group_one,group_two,group_tree
urlpatterns = [
    path("index/",group_one),
    path("order/",group_two),
    path("base/",group_tree),
]