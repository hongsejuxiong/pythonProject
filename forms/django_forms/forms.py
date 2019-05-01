# @ProjectName: forms
# @Author: admin
# @CreateTime: 2019/5/1 下午12:49

from django import forms as DForms
from django.forms import widgets

class DetailForm(DForms.Form):

    user1 = DForms.CharField()
    user2 = DForms.CharField(widget=widgets.PasswordInput(attrs={'class':'csl','placeholder':'苏维埃'}))
    user3 = DForms.ChoiceField(choices=[(1,'列宁'),(2,'斯大林'),(3,'赫鲁晓夫')])