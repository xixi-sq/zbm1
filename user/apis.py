from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse
from common.token_ import create_token, check_token
from libs.http import render_json
from user.forms import UserFrom
from user.logics import check_permission
from user.models import User, Role
import json




def login(request):
    '''登陆'''

    # 是否用account_name待定，没有设置唯一键
    print('----------',request.META.get('HTTP_AUTHORIZATION'))
    # print(request.META)

    account_name = request.POST.get('account_name')
    user_password = request.POST.get('user_password')



    user = User.objects.filter(account_name=account_name).first()

    if not user:
        return render_json(code=100,data=None,message='用户名错误')
    password = user.user_password
    if user_password == password:

        token = create_token(user.id)
        result = {
            'code': 1,
            'data' : None,
            'message': '验证成功',
            'token':token,
        }

        return HttpResponse(json.dumps(result))
    else:
        return render_json(code=0, data=None,message='密码错误')





# def register(request):
#     '''注册用户'''
#     # -------------------------------------------------------
#     '''验证用户是否有注册权限'''
#     user = request.user





    # uid = request.POST.get('uid')
    # user = User.objects.filter(id=uid).first()
    #
    # # 获取当前用户的角色列表
    # role_ids = user.user_role_ids
    # role_ids_list = role_ids.split(',')
    # # roles = Role.objects.filter(id__in = role_ids_list)
    # # -------------确定角色的权限---------
    #
    # a = str(1)  # 假定的角色id,且为字符串类型
    #
    # if a in role_ids_list:
    #
    #     user = request.user
    #
    #     user_form = UserFrom(request.POST)
    #
    #     # 检查用户资料的数据
    #     if not user_form.is_valid():
    #         return render_json(user_form.errors, code=104, data='注册信息不正确')
    #
    #     user.__dict__.update(user_form.cleaned_data)
    #     user.save()
    #
    #
    #
    # else:
    #     return render_json(code=103, data='该用户不能够添加新用户')
    #
    # print(cache.get(uid), '------')
    # # request.POST.get()
    #
    # return render_json(code=102, data='ok')


def test(request):
    return render_json(code=1,message='ok')


