from django.shortcuts import render,HttpResponse,render_to_response
import datetime
from blog import models
# from blog.models import TestData
# from blog.models import Language

from blog.models import Book
from blog.models import Publisher

from blog.models import Author


# from blog.models import *

from django.db.models import Avg,Min,Sum,Max,F,Q


# Create your views here.

# def current_time(request):
#     # return HttpResponse("<h1>OK<h1>")
#     timeParam = datetime.datetime.now()
#
#     return render(request, "currentTime.html", {"current_time": timeParam})
#
#
# userList = []
# def userInfo(request):
#
#     if request.method == "POST":
#         userName = request.POST.get("name", None)
#         userGender = request.POST.get("gender", None)
#         userPhone = request.POST.get("phone", None)
#         userDic = {"name": userName, "gender": userGender, "phone": userPhone}
#         userList.append(userDic)
#
#         models.UserInfo.objects.create(
#             name=userName,
#             gender=userGender,
#             phone=userPhone
#         )
#
#         dbUserList = models.UserInfo.objects.all()
#
#     return render(request, "index.html", {"userList": userList})
#
# def special_case_2003(request):
#     return HttpResponse("2003")
#
# def year_archive(request, yearParam, monthParam):
#
#     return HttpResponse(yearParam + " year " + monthParam + " month ")
#
# def name_archive(request, month, year):
#     return HttpResponse(year + " year " + month + " month ")
#
# def login(request):
#
#     if request.method == "POST":
#         name = request.POST.get("userName")
#         pwd = request.POST.get("password")
#
#         if name == "James" and pwd == "123":
#             return HttpResponse("登录成功")
#
#     return render(request, "name.html")
#
# def introduce(request):
#     return HttpResponse("OK")
#
# def showTemplate(request):
#     # value = 'NBA'
#     # value = [1, 22, 333]
#     # value = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#     # value = datetime.datetime.now()
#
#     # class Person:
#     #     def __init__(self,name,age):
#     #         self.name = name
#     #         self.age = age
#     #
#     # value = Person('Jack', 18)
#     #
#
#
#     value1 = 'nba'
#     # value2 = 3
#
#
#     return render(request, 'template.html', {'value': value1})
#     # return render(request, 'template.html', locals())
#
#
# def functionTest(request):
#
#     # value = [1, 22, 333]
#     # value = []
#     value = 4
#     # return render(request, 'login.html', {'value': value})
#     return render(request, 'ordered.html', {'value': value})
#
#     # return render_to_response('login.html',locals(), content_type=Requ)
#
# def ordered(request):
#
#     return render(request, 'ordered.html')
#
# def shopping_car(request):
#     return render(request, 'shoppingcar.html')
#
#





def ormHandle(request):

    # models.UserInfo.objects.create(
    #     name='1',
    #     gender='2',
    #     phone='3'
    # )



    # models.TestData.objects.create(
    #     name='sidalin',
    #     # gender='男',
    #     phone='10001'
    # )

    #
    # testData = TestData.objects.create(
    #     name='liening',
    #     phone='10002'
    # )
    #
    # testData.save()
    #
    #
    # dic = {"name":"alex","phone":"9999"}
    # TestData.objects.create(**dic)
    # # peron.save()


    # models.TestData.objects.create(**dic)



    # test = TestData()
    # test.name = 'heluxiaofu'
    # test.phone = '777777'
    # test.save()


    # publisher=Publisher()
    # publisher.name='python'
    # publisher.city='beijing'
    # publisher.save()
    #
    # models.Book.objects.create(
    #     title='python',
    #     price=12,
    #     color='red',
    #     page_num=1,
    #     publisher_id=2
    # )


    # 正向查询

    # book = models.Book.objects.filter(id=2)[0]
    # authors = models.Author.objects.filter(id__gt=3)
    #
    # book.author.add(*authors)

    #反向查询

    # author = models.Author.objects.filter(id=2)[0]
    # books = models.Book.objects.filter(id__gt=1)
    #
    # author.book_set.add(*books)



    # obj_set=models.Book.objects.filter(id__gt=3)
    #
    # obj_set.update(title='c++')
    # obj_set.delete()

    # print(obj_set)
    #
    #
    # # Book.objects.crea
    #
    # Book.objects.create(**{'title':'swift'})
    #


    # obj_set.reverse()

    # objAll = models.Book.objects.all()
    # print(objAll)



    # print(obj_set)
    # print(obj_set.first())



    # Book.objects.create(**{'title':'kotlin'})


    # models.Book.objects.filter(title='kotlin').update(title='golang')

    #
    # obj_set2 = models.Book.objects.filter(id__gt=100)
    # obj_set3 = models.Book.objects.filter(id__lt=3)
    #
    # obj_set3.update(title='JavaScript')
    #
    # if obj_set2.exists():
    #
    #     print("万岁")
    #
    # elif obj_set3.exists():
    #     # print('long live')
    #     print(obj_set3)
    # else:
    #     print('乌拉')


    # obj = models.Book.objects.filter(id=2)[0]
    # print(obj.publisher.city)


    # pub = models.Publisher.objects.filter(city='beijing')
    # # print(pub.book_set.all())
    #
    # print(models.Publisher.objects.filter(city='tianjin').values('name'))


    # obj = models.Publisher.objects.filter(id=2)[0]
    #
    # print(obj.book_set.all().distinct().values("title"))



    # print(models.Publisher.objects.filter(book__title='swift',book__id=8).values('name').distinct())

    # print(models.Book.objects.filter(title='swift').values('publisher__name').distinct())

    #
    # print(models.Publisher.objects.filter(city='beijing').values('name'))
    #
    # print(models.Book.objects.filter(publisher__city='beijing').values('publisher__name'))


    obj = models.Book.objects.all().aggregate(Avg('price'))
    obj2=Book.objects.all().aggregate(Max('price'))
    obj3=Book.objects.all().aggregate(Sum('price'))
    obj4=Book.objects.all().aggregate(myPrice=Avg('price'))
    obj5=Book.objects.aggregate(myPrice=Avg('price'))
    obj6=Book.objects.all().aggregate(Avg('price'),Sum('price'),Max('price'),Min('price'))
    obj7=Book.objects.all().aggregate(myAvg=Avg('price'),mySum=Sum('price'),myMax=Max('price'),myMin=Min('price'))
    # obj8=Publisher.objects.values(book__name='swift').aggregate(Sum('price'))
    # obj9=models.Publisher.objects.filter(book__title='swift').values('book__price')
    # obj10=Publisher.objects.values(city='beijing').annotate(Sum('price'))

    # obj11=Publisher.objects.values('book__title').annotate(Sum('price'))
    # obj12=Book.objects.values('publisher__city').annotate(Sum('price'))


    # models.Book.objects.all().update(price=F('price')+10)


    # obj13=models.Book.objects.filter(Q(id__gt=4)|Q(title='ruby')&Q(id__lt=9),color='red')
    # obj14=models.Book.objects.filter(Q(title__startswith='p')|Q(id__gt=14))
    #
    # obj15=models.Book.objects.get(title='php')


    # print(obj)
    # print(obj2)
    # print(obj3)
    # print(obj4)
    # print(obj5)
    # print(obj6)
    # print(obj7)
    # print(obj8)
    # print(obj12)

    print(obj15)


    return render(request, 'ormHandle.html')

































