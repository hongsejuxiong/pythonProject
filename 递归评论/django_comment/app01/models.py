from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)

class News(models.Model):
    title = models.CharField(max_length=32)

class Comment(models.Model):
    content = models.CharField(max_length=32)
    user_info = models.ForeignKey('UserInfo')
    news = models.ForeignKey('News')
    parent = models.ForeignKey("self",related_name='o',null=True)
    ctime = models.DateTimeField(auto_now_add=True,null=True)




