from django.db import models

# Create your models here.

# Book

class Book(models.Model):
    '''Book model class'''
    # 字符串
    # max_length ： 最大长度
    title = models.CharField(max_length=40)
    # pub date
    # date type
    pub_date = models.DateField()

    def __str__(self):
        return self.title






