from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)



class Person(models.Model):
    name = models.CharField(max_length=64)
    # age = models.IntegerField(max_length=64)
    # gender = models.BooleanField()
    phone = models.CharField(max_length=64)

    # height = models.FloatField(max_di)

class TestData(models.Model):
    name = models.CharField(max_length=64)
    # age = models.IntegerField(max_length=64)
    # gender = models.BooleanField()
    phone = models.CharField(max_length=64)

    # height = models.FloatField(max_di)

class Book(models.Model):
    title=models.CharField(max_length=64,default="")
    price=models.IntegerField(default=0)
    color=models.CharField(max_length=64,default="")
    page_num=models.IntegerField(default=0)

    # publisher=models.ForeignKey('Publisher',on_delete=models.CASCADE,related_name='append_publisher',default=1)
    # publisher=models.ForeignKey('Publisher')

    publisher=models.ForeignKey('Publisher',on_delete=models.CASCADE)


    #
    author=models.ManyToManyField('Author')


    def __str__(self):
        return self.title


class Publisher(models.Model):
    name=models.CharField(max_length=64,default="")
    city=models.CharField(max_length=64,default="")
    # book=models.ForeignKey('Book',default=1,on_delete=models.CASCADE,related_name='append_book')
    # book=models.ForeignKey('Book')

    def __str__(self):
        return self.city



class Author(models.Model):
    name=models.CharField(max_length=64,default="")
    title=models.CharField(max_length=64,default="")
    time=models.CharField(max_length=64, default="")

    def __str__(self):
        return self.name

class Language(models.Model):
    title = models.CharField(max_length=64, default="0")
    # price = models.IntegerField()
    # color = models.CharField(max_length=64)
    # page_num = models.IntegerField()


# class Book2Author(models.Model):
#     # author=models.ForeignKey('Author')
#     author=models.ForeignKey('Author',default=1,on_delete=models.CASCADE,related_name='append_author')
#
#     # book=models.ForeignKey('Book')
#
#     book=models.ForeignKey('Book',default=1,on_delete=models.CASCADE,related_name='append_book')




class Country(models.Model):
    name=models.CharField(max_length=64,default="")
    # =models.CharField(max_length=64,default="")
    # book=models.ForeignKey('Book',default=1,on_delete=models.CASCADE,related_name='append_book')
    # book=models.ForeignKey('Book')



class State(models.Model):
    name=models.CharField(max_length=64,default="")
    title=models.CharField(max_length=64,default="")
    country=models.ForeignKey('Country',on_delete=models.CASCADE)



