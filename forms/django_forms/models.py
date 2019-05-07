from django.db import models

# Create your models here.


class UserType(models.Model):

    user_type = models.CharField(max_length=32)