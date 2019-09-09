from django.db import models

# Create your models here.
from libs.http import render_json


class User(models.Model):
    '''用户'''
    account_name = models.CharField(max_length=50,unique=True,verbose_name='账号名')   #新增了唯一键
    user_role_ids = models.CharField(max_length=50,verbose_name='角色id')
    user_main_role_id = models.CharField(max_length=50,verbose_name='主要角色id')
    user_org_ids = models.CharField(max_length=50,verbose_name='组织id')
    user_org_type = models.CharField(max_length=50,verbose_name='组织类型')
    user_name = models.CharField(max_length=50,verbose_name='用户名')
    user_sex = models.CharField(max_length=50,verbose_name='用户性别')
    user_password = models.CharField(max_length=50,verbose_name='密码')
    user_phone = models.CharField(max_length=50,verbose_name='手机号')

    # @property
    # def user_roles(self):
    #     '''用户的角色'''
    #
    #     self.user_roles = Role.objects.get(id__in = list(self.user_role_ids))
    #     if not self.user_roles :
    #         return render_json(code=0,data=None,message='该用户没有权限')
    #     print(self.user_roles,'---------')
    #     return self.user_roles
    #
    # @property
    # def user_main_role_id(self):
    #     '''用户的主要角色'''
    #     self.user_main_role_id = Role.objects.get(id=self.user_main_role_id)
    #     return self.main_role_id
    #
    # @property
    # def org(self):
    #     '''用户组织id'''
    #     if not hasattr(self, 'org'):
    #         self.org= Role.objects.get(id=self.user_org_ids)
    #         return self.org


    class Meta:
        db_table = 'user'

    def to_dict(self):
        return {
            'account_name' :self.account_name ,
            'user_role_ids' :self.user_role_ids ,
            'user_main_role_id' :self.user_main_role_id ,
            'user_org_ids' :self.user_org_ids ,
            'user_org_type' :self.user_org_type ,
            'user_name' :self.user_name ,
            'user_sex' :self.user_sex ,
            'user_password' :self.user_password ,
            'user_phone' :self.user_phone ,
        }

class Role(models.Model):
    '''角色'''
    role_name = models.CharField(max_length=50,verbose_name='角色名称')
    role_pid = models.CharField(max_length=50,verbose_name='pid')
    role_code = models.CharField(max_length=50,verbose_name='角色编码')
    # role_power_ids = models.CharField(max_length=50,verbose_name='权限id')
    role_remark = models.CharField(max_length=50,verbose_name='备注/功能')

    def permissions(self):
        '''查看当前用户拥有的权限'''
        perm_id_list = RolePermRelation.objects.filter(Role_id = self.id).value_list('perm_id',flat = True)
        return Permission.objects.filter(id__in = perm_id_list)


    def has_permission(self,perm_name):
        '''检查当前用户是否具有某权限'''
        perm_name_list = self.permissions().values_list('name',flat=True)   #拥有所有的权限名字
        return perm_name in perm_name_list

    class Meta:
        db_table = 'role'

    def to_dict(self):
        return {
            'role_name' : self.role_name ,
            'role_pid' : self.role_pid ,
            'role_code' : self.role_code ,
            # 'role_power_ids' : self.role_power_ids ,
            'role_remark' : self.role_remark ,
        }

class Permission(models.Model):
    '''权限表'''
    Permission_pid = models.CharField(max_length=50,verbose_name='pid')
    Permission_code = models.CharField(max_length=50,verbose_name='权限编码')
    Permission_name = models.CharField(max_length=50,verbose_name='权限名称')
    Permission_remark = models.CharField(max_length=50,verbose_name='权限功能')
    Permission_type = models.CharField(max_length=50,verbose_name='1菜单权限/2按钮权限（数据权限/代码实现）')

    class Meta:
        db_table = 'power'

    def to_dict(self):
        return {
            'power_pid' : self.Permission_pid ,
            'power_code' : self.Permission_code ,
            'power_name' : self.Permission_name ,
            'power_remark' : self.Permission_remark ,
            'power_type' : self.Permission_type ,
        }


class RolePermRelation(models.Model):
    '''角色权限关系表'''

    role_id = models.CharField(max_length=50,verbose_name='角色 ID')
    perm_id = models.CharField(max_length=50,verbose_name='权限 ID')
