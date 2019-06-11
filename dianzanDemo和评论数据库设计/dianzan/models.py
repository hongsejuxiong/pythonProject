from django.db import models

# Create your models here.


class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField()

class NewsType(models.Model):
    caption = models.CharField(max_length=6)

class News(models.Model):
    title = models.CharField(max_length=32)
    summary = models.CharField(max_length=128, null=True)
    url = models.URLField(null=True)
    ctime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to="UserInfo", to_field='nid', related_name='news')
    news_type_choices = [
        (1, '42区'),
        (2, '段子'),
        (3, '图片'),
    ]

    nt = models.IntegerField(choices=news_type_choices)


    favor_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    favor = models.ManyToManyField(to='UserInfo')


# class Favor(models.Model):
#     news = models.ForeignKey(to='News', to_field='id')
#     user = models.ForeignKey(to='UserInfo', to_field='nid')



class Comment(models.Model):
    news = models.ForeignKey(to='News', to_field='id')
    user = models.ForeignKey(to='UserInfo', to_field='nid')
    content = models.CharField(max_length=150)
    device = models.CharField(max_length=16, null=True)
    ctime = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(to='self', null=True, related_name='cp')



"""
====================== 新闻评论 ====================== 

自增id    用户名     新闻id      评论内容                    父评论

 1        James      11          dssafsaf                  null
 2        Kobe       22          ewqewqweq                 null
 3        Yao        33          afwefewqe                 null
 4        James      22          dhfgdfg                   2(Kobe的自增id,不仅评论了新闻内容,还回复了评论人,所以要记住父评论的id)
 5        James      33          bdfgbsdre                 3(Yao的自增id)
 6        James      44          iuokyuiuku                null


"""