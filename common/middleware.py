
from django.utils.deprecation import MiddlewareMixin

from common.token_ import get_username, check_token
from libs.http import render_json
from user.models import User
from django.core.cache import cache

class AuthMiddleware(MiddlewareMixin):
    API_WHITE_LIST = [
        '/zbm/user/login/',


    ]

    def process_request(self, request):

        if request.path in self.API_WHITE_LIST:
            return
        # print(request.META)
        token = request.META.get('HTTP_TOKEN')

        #返回用户id
        id =get_username(token)
        #判断用户是否登录
        account_name = check_token(token)




        if not account_name:
            return render_json(code=0,data=None,message='账号未登录')
        else:
            request.user = User.objects.get(id=id)



