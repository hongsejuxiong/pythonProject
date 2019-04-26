from django.shortcuts import render,HttpResponse

# Create your views here.


def myIndex(req):


    return render(req,'myIndex.html')


def myAjax(req):

    return HttpResponse('hello')
