from django.db import models

# Create your models here.

class Org(models.Model):
    '''组织表'''
    org_pid = models.CharField(max_length=50,verbose_name='pid')
    org_code = models.CharField(max_length=50,verbose_name='组织编码')
    org_name = models.CharField(max_length=50,verbose_name='组织名称')
    org_location = models.CharField(max_length=50,verbose_name='组织位置/街道信息')
    org_longitude = models.CharField(max_length=50,verbose_name='经度')
    org_latitude = models.CharField(max_length=50,verbose_name='纬度')
    org_outline = models.CharField(max_length=50,verbose_name='轮廓')
    org_leader_name = models.CharField(max_length=50,verbose_name='负责人')
    org_leader_phone = models.CharField(max_length=50,verbose_name='负责人电话')
    org_is_entity = models.CharField(max_length=50,verbose_name='1区域范围/2公司或部门/3小区')

    class Meta:
        db_table = 'org'
        
    def to_dict(self):
        return {
            'org_pid' : self.org_pid ,
            'org_code' : self.org_code ,
            'org_name' : self.org_name ,
            'org_location' : self.org_location ,
            'org_longitude' : self.org_longitude ,
            'org_latitude' : self.org_latitude ,
            'org_outline' : self.org_outline ,
            'org_leader_name' : self.org_leader_name ,
            'org_leader_phone' : self.org_leader_phone ,
            'org_is_entity' : self.org_is_entity ,
        }


class Building(models.Model):
    '''单元楼'''
    buliding_code = models.CharField(max_length=50,verbose_name='楼宇编码')
    buliding_name = models.CharField(max_length=50,verbose_name='楼宇名称')
    buliding_addr = models.CharField(max_length=50,verbose_name='小区地址/街道信息')
    buliding_img = models.CharField(max_length=50,verbose_name='图片/给的是图片存储路径')
    buliding_family_count = models.CharField(max_length=50,verbose_name='多少户')
    buliding_height = models.CharField(max_length=50,verbose_name='楼的高度')
    buliding_kind = models.CharField(max_length=50,verbose_name='建筑类型/住宅/商业')
    buliding_type = models.CharField(max_length=50,verbose_name='建筑物结构类型1/2/3/')
    buliding_create_time = models.CharField(max_length=50,verbose_name='创建时间')
    buliding_create_unit = models.CharField(max_length=50,verbose_name='创建单位')
    buliding_org_id = models.CharField(max_length=50,verbose_name='所属组织')
    buliding_remarks = models.CharField(max_length=50,verbose_name='备注')

    class Meta:
        db_table = 'building'

    def to_dict(self):
        return {
            'buliding_code' : self.buliding_code ,
            'buliding_name' : self.buliding_name ,
            'buliding_addr' : self.buliding_addr ,
            'buliding_img' : self.buliding_img ,
            'buliding_family_count' : self.buliding_family_count ,
            'buliding_height' : self.buliding_height ,
            'buliding_kind' : self.buliding_kind ,
            'buliding_type' : self.buliding_type ,
            'buliding_create_time' : self.buliding_create_time ,
            'buliding_create_unit' : self.buliding_create_unit ,
            'buliding_org_id' : self.buliding_org_id ,
            'buliding_remarks' : self.buliding_remarks ,
        }











