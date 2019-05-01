from django.shortcuts import render

# Create your views here.

from django_forms import forms

def detail(request):

    obj = forms.DetailForm()

    return render(request, 'detail.html', {'obj':obj})