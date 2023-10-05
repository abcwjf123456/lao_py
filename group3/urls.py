from group3 import views
from django.urls import re_path,path
urlpatterns=[
    path('',views.index),
    path('index1/',views.index1),

]

