from django.shortcuts import render

# Create your views here.


def test(request):

    from django.core.handlers.wsgi import WSGIRequest

    print(type(request))
    # print(request.environ)
    print(request.environ.get('HTTP_USER_AGENT'))

    return render(request,'test.html')