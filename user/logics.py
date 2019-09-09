from libs.http import render_json


def check_permission(perm_id):
    '''权限装饰器'''
    def deco(view_func):
        def wrap(request,*args,**kwargs):
            user = request.user
            if user.user_roles.has_permission(perm_id):
                return view_func(request,*args,**kwargs)
            else:
                return render_json(code=0,message='该用户没有权限')
        return wrap
    return deco

