
from django.contrib import admin
from django.urls import path,re_path,include
from blog import views

urlpatterns = [

    re_path(r'news/story/$', views.introduce)
    # path('news/story/', views.introduce)
]
