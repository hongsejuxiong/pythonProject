from django.db import models

# Create your models here.


class Classes(models.Model):
    caption = models.CharField(max_length=32)


class Teacher(models.Model):

    name = models.CharField(max_length=32)
    cls = models.ManyToManyField('Classes')


class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32, null=True)
    cls = models.ForeignKey('Classes', on_delete=models.CASCADE)


class Administrator(models.Model):
    username = models.CharField(max_length=32)

    password = models.CharField(max_length=32)


class Province(models.Model):
    name = models.CharField(max_length=32)
    brief = models.CharField(max_length=32, default='')

class City(models.Model):
    name = models.CharField(max_length=32)
    pro = models.ForeignKey('Province', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=32)
    m = models.ManyToManyField('Author')

    def __str__(self):
        return self.name

class Img(models.Model):
    file_path = models.CharField(max_length=128)
