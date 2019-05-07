# @ProjectName: forms
# @Author: admin
# @CreateTime: 2019/5/1 下午12:49

from django import forms as DForms
from django.forms import widgets,fields


class DetailForm(DForms.Form):

    user1 = fields.CharField(min_length=4, error_messages={'required':'用户名不能为空'})
    user2 = fields.CharField(widget=widgets.TextInput(attrs={'class':'csl','placeholder':'苏维埃'}))
    user3 = fields.ChoiceField(choices=[(1,'列宁'),(2,'斯大林'),(3,'赫鲁晓夫')])
    user4 = fields.CharField(widget=widgets.Select(
        choices=[(1,'俄罗斯'),(2,'乌克兰'), (3,'白罗斯')]
    ))
    user4 = fields.IntegerField(widget=widgets.Select(
        choices=[(1,'俄罗斯'),(2,'乌克兰'), (3,'白罗斯')]
    ))
    user5 = fields.IntegerField(widget=widgets.RadioSelect(
        choices=[(1,'加里宁'),(2,'托洛茨基'),(3,'图哈切夫斯基')]

    ))


from django_forms import models
class DBForm(DForms.Form):

    user_name = fields.CharField()
    # user_type0 = fields.IntegerField(widget=widgets.Select(choices=models.))
    user_type = fields.IntegerField(widget=widgets.Select(choices=[]))

    def __init__(self, *args, **kwargs):
        super(DBForm, self).__init__(*args, **kwargs)

        self.fields['user_type'].widget.choices = models.UserType.objects.all().values_list('id', 'user_type')