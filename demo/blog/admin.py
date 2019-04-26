from django.contrib import admin
from django.db import models
from blog.models import *

# Register your models here.
#
class Myadmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'publisher')
    # search_fields = ('title')
    search_fields = ('title','price')


admin.site.register(Book,Myadmin)