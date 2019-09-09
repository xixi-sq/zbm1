from django.db import models

# Create your models here.
class Constant_id(models.Model):
    '''常量'''
    constant_name = models.CharField(max_length=50,verbose_name='常量名称,目前有LEC')

    class Meta:
        db_table = 'constant'

class Constant(models.Model):
    '''常量内容'''
    constant_type = models.CharField(max_length=50,verbose_name='常量类型')
    constant_score = models.CharField(max_length=50,verbose_name='分值')
    constant_key = models.CharField(max_length=50,verbose_name='常量描述')