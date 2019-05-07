from django.shortcuts import render

# Create your views here.

from django_forms import forms

def detail(request):

    if request.method == 'GET':
        obj = forms.DetailForm()

        return render(request, 'detail.html', {'obj': obj})
    else:

        obj = forms.DetailForm(request.POST)

        if obj.is_valid():
            print(obj.clean())




def db(request):
    
    obj = forms.DBForm()
    return render(request, 'db.html', {'obj': obj})



