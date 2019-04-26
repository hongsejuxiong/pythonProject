from django.shortcuts import render,HttpResponse
import json
# Create your views here.


def register(req):

    return render(req,'register.html')


def ajax_register(req):



    if req.method == 'POST':
        value = req.POST.get('userName')
        print(value)
        if value == 'alex':
            return HttpResponse('1')
        else:
            return HttpResponse('0')


    return render(req, 'register.html')


def ajax_get(req):

    # test = req.POST.get
    test = req.POST


    print(test)

    dic = {'name':'sss', 'age': 10, 'gender': 'male'}


    data = json.dumps(dic)
    print(data)

    # HttpResponse.status_code = 400





    return HttpResponse(data)










def ajax_test(req):

    return render(req, 'ajax_test.html')