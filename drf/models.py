from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=32, verbose_name="书籍名称")
    owned_date = models.DateField(verbose_name="拥有日期", null=True)
    current_position = models.CharField(max_length=255, verbose_name="当前存储位置(描述)")
    reading_process = models.CharField(max_length=255, verbose_name="阅读进程(描述)")
    readings = models.IntegerField(default=0, verbose_name="阅读次数")
    remove_status = models.BooleanField(default=False, verbose_name="移除状态")
    """ 注意：字段默认写入不允许为空的，但字符串类型如果没有传入值默认会使用空字符串，没有受到默认的null=False(不允许为null，即不传)的约束 """
    class Meta:
        db_table = 'book'


class User(models.Model):
    name = models.CharField(max_length=255, verbose_name="昵称")
    age = models.IntegerField(verbose_name="年龄")
    address = models.CharField(max_length=255, verbose_name="地址")

    class Meta:
        db_table = 'user'


