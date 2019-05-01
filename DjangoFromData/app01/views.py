from django.shortcuts import render, HttpResponse

# Create your views here.

from django import forms

class MyFormData(forms.Form):
    user = forms.CharField(min_length=6,error_messages={'min_length':'用户名长度最小为6', 'required':'用户名不能为空'})
    email = forms.EmailField(error_messages={'invalid': '邮箱格式错误','required':'邮箱不能为空'})

class TestFormData(forms.Form):
    user = forms.CharField(min_length=6,error_messages={'min_length':'用户名长度最小为6', 'required':'用户名不能为空'})
    email = forms.EmailField(error_messages={'invalid': '邮箱格式错误','required':'邮箱不能为空'})
    favor = forms.MultipleChoiceField(
        choices=[(1,'列宁'),(2,'斯大林'),(3,'赫鲁晓夫')]
    )


def login(request):
    if request.method == 'GET':
        obj = MyFormData()
        return render(request, 'login.html', {'obj':obj})
    else:

        form_obj = MyFormData(request.POST)

        # 如果验证成功
        if form_obj.is_valid():
            #获取验证后的值
             obj = form_obj.clean()
             print(obj)

        else:

            errors = form_obj.errors
            print(errors)
            print(errors.as_json())
            print(errors['user'])
            print(errors['email'])


        return render(request, 'login.html',{'obj':form_obj})

import json
def ajax_login(request):

    if request.method == 'GET':


        return render(request, 'ajax_login.html')

    else:

        obj = MyFormData(request.POST)

        dic = {'status': True, 'data': None, 'error': None}

        if obj.is_valid():
            dic['data'] = obj.clean()
            return HttpResponse(json.dumps(dic))

        else:
            # dic['error'] = obj.errors.as_json()

            dic['error'] = obj.errors.as_data()

            print(obj.errors.as_data())

            dic['status'] = False
            return HttpResponse(json.dumps(dic, cls=JsonCustomEncoder))


from django.core.validators import ValidationError

class JsonCustomEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ValidationError):
            return {'code': o.code, 'message':o.message}
        else:
            return json.JSONEncoder.default(self, o)


def index(request):

    formData = TestFormData({'user':'苏维埃','email':'wansui@suweiai.com','favor':[1,2]})

    return render(request, 'index.html',{'formData':formData})
