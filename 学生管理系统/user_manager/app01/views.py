from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from django import views
# Create your views here.


def login(req):

    # models.Administrator.objects.create(
    #     username='root',
    #     password='123'
    # )

    message = ''
    if req.method == 'POST':

        username = req.POST.get('user')
        password = req.POST.get('pwd')

        count = models.Administrator.objects.filter(password="1223",username=username).count()

        print('数量')
        print (count)

        if count :
        # if username == 'root' and password == '123':

            req.session['is_login'] = True
            req.session['username'] = username


            ret = redirect('base.html')
            print('万岁')

            return redirect('base.html')
        else:
            message = '用户名或密码错误'

    return render(req, 'login.html', {'message':message})


# if username == 'root' and password == '123':
# # if count:
#     ret = redirect('base.html')
#     ret.set_cookie('username', username,max_age=2,path='/')
#     ret.set_cookie('username', username)
#
#     ret.set_cookie('test','testData')
#     return ret


def logout(request):
    request.session.clear()
    return render(request,'login.html')


def index(req):

    # username = req.COOKIES.get('username')
    # print('用户名')

    username = req.session['username']

    print(username)
    if username:
        return render(req, 'base.html', {'username':username})
    else:
        return redirect('login.html')


def test(req):
    username = req.COOKIES.get('username')
    return render(req,'test.html',{'username':username})

def cookie(request):

    # print(request.COOKIES)
    print(request.session)
    request.session.setdefault('k5','v5')
    request.session['name'] = 'alex'
    red = render(request,'cookie.html')
    red.set_cookie('k2','v2')

    return red


def outer(func):
    def inner(request, *args, **kwargs):
        print(request.method)
        return func(request, *args, **kwargs)
    return inner

from django.utils.decorators import method_decorator

class Login(views.View):

    # @method_decorator(outer)


    def dispatch(self, request, *args, **kwargs):

        print('111')

        ret = super(Login,self).dispatch(self,request,)

        print('222')

    def get(self, request, *args, **kwargs):

        print(request.method)
        return render(request, 'login.html', {'message': ''})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('user')
        password = request.POST.get('pwd')

        c = models.Administrator.objects.filter(username=username, password=password).count()

        if c:
            request.session['is_login'] = True
            request.session['username'] = username

            ret = redirect('base.html')

            return ret
        else:
            message = '用户名或密码错误'
            return render(request,'login.html', {'message':message})

import json

def handle_classes(request):


    if request.method == 'GET':

        user_name = request.session.get('username')

        cls_list = models.Classes.objects.all()

        return render(request, 'classes.html', {'username': user_name, 'cls_list':cls_list})

    else :
        captionValue = request.POST.get('caption', None)
        response_dic = {'status': True, 'error': None, 'data': None}

        if captionValue:

            obj = models.Classes.objects.create(caption=captionValue)
            response_dic['data'] = {'id': obj.id, 'caption': obj.caption}
        else:
            response_dic['status'] = False
            response_dic['error'] = '标题不能为空'

        return HttpResponse(json.dumps(response_dic))




"""

        if request.method == 'GET':

        user_name = request.session.get('username')

        cls_list = models.Classes.objects.all()

        return render(request, 'classes.html', {'username': user_name, 'cls_list':cls_list})

    elif request.method == 'POST':

            caption = request.POST.get('caption')

            if caption:
                models.Classes.objects.create(caption=caption)

            return redirect('classes.html')


"""

"""

def handle_addClasses(request):

    msg = ""

    if request.method == 'GET':

        return render(request, 'addClasses.html', {'msg': msg})

    elif request.method == 'POST':

        caption = request.POST.get('caption', None)

        if caption:
            models.Classes.objects.create(caption=caption)
            return redirect('classes.html')


        else:
            msg = '内容不能为空'
            return render(request, 'addClasses.html', {'msg': msg})


    else:
        return render(request, 'base.html')

"""


def handle_addClasses(request):

    msg = ''
    if request.method == 'GET':
        return render(request, 'addClasses.html', {'msg': msg})
    elif request.method == 'POST':
        caption = request.POST.get('caption', None)
        if caption:

             models.Classes.objects.create(caption=caption)
             return redirect('/classes.html')
        else:

            msg = '内容不能为空'
            return render(request, 'addClasses.html', {'msg': msg})

    else:
        return render(request, 'base.html')





def handle_edit_classes(request):

    msg = ''

    if request.method == 'POST':

        nid = request.POST.get('nid', None)
        caption = request.POST.get('caption', None)

        if caption:
            models.Classes.objects.filter(id=nid).update(caption=caption)
            return redirect('/classes.html')
        else:
            msg = '标题不能为空'
            return render(request, 'editClasses.html', {'msg':msg})



    elif request.method == 'GET':

        nid = request.GET.get('nid', None)

        obj = models.Classes.objects.filter(id=nid).first()

        return render(request, 'editClasses.html', {'obj':obj})
    else:

        return redirect('login.html')




def handle_student(request):

    student_list = models.Student.objects.all()


    return render(request, 'student.html', {'student_list':student_list})



def handle_edit_student(request):

    if request.method == 'GET':

        nid = request.GET.get('nid', None)
        obj = models.Student.objects.filter(id=nid).first()

        cls_list = models.Classes.objects.all()

        return render(request, 'edit_student.html', {'cls_list':cls_list, 'obj':obj})


    elif request.method == 'POST':
        nid = request.POST.get('nid', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        cls__caption = request.POST.get('classes', None)
        # cls_obj = models.Classes.objects.filter(caption=cls__caption).first().id
        clsID = models.Classes.objects.filter(caption=cls__caption).first().id
        # clsID = cls_obj.id


        print(nid, name, email, clsID)

        models.Student.objects.filter(id=nid).update(name=name,email=email,cls=clsID)

        data = {'resultData':True}

        return redirect('student.html')
        # return HttpResponse(data)
    else:
        return redirect('login.html')



def handle_database(request):



    # models.Province.objects.create(
    #     name='河南',
    #     brief='豫',
    # )

    # testData = {'name':'河北','brief':'冀'}

    # models.Province.objects.create(**{
    #     'name':'北京',
    #     'brief':'京',
    # })

    # models.Province.objects.create(**testData)


    # pro_name = models.City.objects.filter(name="开封").first().pro.name

    # print(pro_name)


    # # data =  models.City.objects.values('name','id','pro__brief','pro__name').all()
    # data =  models.City.objects.values('name','id','pro__brief','pro__name')
    # data_name =  models.City.objects.values('name')
    # # data_list = models.City.objects.values_list('name','pro__brief')
    # data_list = models.City.objects.values_list('name')
    #
    # filter_name = models.City.objects.filter(id__lt=2).values('name')
    # # print(data)
    #
    # # print(data_name)
    # # print(data_list)
    # print(filter_name)


    # book_obj = models.Book.objects.filter(name='三国演义').values('m__book__name')
    # book_obj = models.Book.objects.filter(name='三国演义').all()
    # book_obj = models.Book.objects.get(name='水浒传')
    # author_all = book_obj.m.all()
    # print(author_all)

    #
    # author_obj = models.Author.objects.get(name='罗贯中')
    #
    #
    # for item in author_obj.book_set.all():
    #     # print(('书名: %s' % (item)))
    #     print('书名: %s' %(item))
    # # print(author_obj.book_set[0].name)


    obj = models.Book.objects.get(id=1)

    #添加对应关系,给书添加作者
    # obj.m.add(3)
    # obj.m.add(2,4)
    # obj.m.add(*[1,2,3,4])

    # 覆盖对应关系
    # obj.m.set([2,3])

    # 删除
    # obj.m.remove(2)
    # obj.m.remove(1,4)
    # obj.m.remove(*[1,4])

    # 清空
    # obj.m.clear

    # 反向设置
    # obj_set = models.Author.objects.get(id=1)
    # obj_set.book_set.add(3,4)
    # .....


    return HttpResponse('OK')



def handle_teacher(request):

    # teacher_list = models.Teacher.objects.all()
    # teacher_list = models.Teacher.objects.filter(id__in=models.Teacher.objects.all()[0:5]).values('id', 'name', 'cls__id', 'cls__caption')
    teacher_list = models.Teacher.objects.values('id', 'name', 'cls__id', 'cls__caption')
    result = {}

    for item in teacher_list:

        if item['id'] not in result:

            tmp = []
            if item['cls__id']:
                tmp = [{'cls__id':item['cls__id'], 'cls__caption':item['cls__caption']}]

            result[item['id']] = {
                'id': item['id'],
                'name': item['name'],
                'cls': tmp
            }

        else:

            if item['cls__id']:
                result[item['id']]['cls'].append({'cls__id':item['cls__id'], 'cls__caption':item['cls__caption']})

    # print(teacher_list.count())
    # print(teacher_list)
    print(result)
    return render(request,'teacher.html', {'teacher_list':teacher_list,'result':result })


def handle_edit_teacher(request, nid):
    obj = models.Teacher.objects.get(id=nid)

    if request.method == 'GET':

        class_name = obj.name

        # cls_list = models.Classes.objects.all().values('caption')
        cls_list = models.Classes.objects.all()

        teacher_cls_list = obj.cls.all().values_list('id', 'caption')

        #list(zip(*list)),将数组中的元组中的每一项取出,添加到一起,组成新的数组
        tmp_list = list(zip(*teacher_cls_list))
        #[(1, 8, 9), ('测试一', '测试二', '测试三')]

        id_list = tmp_list[0]
        #(1, 8, 9)

        # id_not_list0 = models.Classes.objects.exclude(id__in=id_list).values_list('id')
        class_not_list = models.Classes.objects.exclude(id__in=id_list)
        # teacher_not_list = list(zip(*id_not_list0))[0]

        # caption_list = list[1]
        #('测试一', '测试二', '测试三')

        # print(id_list)

    elif request.method == 'POST':

        name = request.POST.get('name')
        selected_list = request.POST.getlist('classes')
        print(selected_list)
        obj.name = name
        obj.save()

        obj.cls.set(selected_list)

        return redirect('/teacher.html')



    return render(request, 'edit_teacher.html', {'obj':obj, 'cls_list':cls_list, 'id_list':id_list, 'class_not_list':class_not_list})

import os,json
def upload(request):

    if request.method == 'GET':

        img_list = models.Img.objects.all()
        return render(request, 'upload.html', {'img_list':img_list})
    elif request.method == 'POST':

        upload_name = request.POST.get('name')
        file_obj = request.FILES.get('image')


        """
            只能获取文件的名字:
            file_name = request.POST.get('image')
        """
        file_path = os.path.join('static', 'upload', file_obj.name)

        f = open(file_path, 'wb')
        for chuck in file_obj.chunks():
            f.write(chuck)

        f.close()

        models.Img.objects.create(file_path=file_path)

        # return redirect('/upload.html')

        dic = {'status': True, 'file_path': file_path}

        return HttpResponse(json.dumps(dic))

