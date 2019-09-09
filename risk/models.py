from django.db import models

# Create your models here.

class Risk(models.Model):
    '''风险类型前端让巡检人员选择'''
    buliding_risk_grade = models.CharField(max_length=50,verbose_name='风险等级')
    buliding_risk_kind_big = models.CharField(max_length=50,verbose_name='风险大类')
    buliding_risk_kind_big_code = models.CharField(max_length=50, verbose_name='风险大类编码')
    buliding_risk_kind_small = models.CharField(max_length=50,verbose_name='风险小类')
    buliding_risk_kind_small_code = models.CharField(max_length=50,verbose_name='风险小类编码')
    buliding_risk_index = models.CharField(max_length=50,verbose_name='风险指数')

    class Meta:
        db_table = 'risk'

    def to_dict(self):
        return {
            'buliding_risk_grade' : self.buliding_risk_grade ,
            'buliding_risk_kind_big' : self.buliding_risk_kind_big ,
            'buliding_risk_kind_big_code' : self.buliding_risk_kind_big_code ,
            'buliding_risk_kind_small' : self.buliding_risk_kind_small ,
            'buliding_risk_kind_small_code' : self.buliding_risk_kind_small_code ,
            'buliding_risk_index' : self.buliding_risk_index ,
        }


class data(models.Model):
    '''上传的数据表以及风险等级'''
    location                位置信息街道
    org_id                  组织id
    risk_big_code           风险大类编码
    risk_small_code         风险小类编码
    constant_type           风险类型/L/E/C
    constant_score          风险分值
    风险指数
    status                  状态1是提交/2是审核转接审核信息表/3是以处理转接处理信息表(以处理页面展示)
    people                  上传人
    pelple_phone            上传人联系方式
    time                    上传时间
    项目信息
    线路信息
    工点信息
    数据来源1是智能监控/2是人工巡检/3是群测群防
    备注




class 处理表(models.Model):
    处理人
    处理时间
    处理状态1是代解决/2是处理中/3是处理完成/4是



