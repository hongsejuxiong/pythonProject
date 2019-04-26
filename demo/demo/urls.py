"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
# from blog import views
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('current_time', views.current_time),
    # path('userInfo', views.userInfo),
    # path('^articles/2003/$', views.special_case_2003)
    # path(r'^articles/2003/$', views.special_case_2003)
    # path('articles/2003', views.special_case_2003),
    # re_path(r'^articles/2003$', views.special_case_2003),
    # re_path(r'^articles/[0-9]{4}/$', views.special_case_2003)
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive)

    # re_path(r'^articles/([0-9]{4})/$', views.year_archive),

    # re_path(r'articles/([0-9]{4})/([0-9]{2})', views.year_archive)

    # re_path(r'articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', views.name_archive),
    # re_path(r'pay/login/', views.login, name="alex")

    # re_path(r'^blog/', include('blog.urls')),

    # path('^blog', include('blog.urls')),
    # re_path(r'showTemplate', views.showTemplate),

    # re_path(r'login', views.functionTest)

    # re_path(r'ordered/', views.ordered),
    # re_path(r'shopping_car/', views.shopping_car),
    # re_path(r'ormHandle/', views.ormHandle),

    path('/myIndex/', views.myAjax),
    path('/myAjax/', views.myAjax),


]

