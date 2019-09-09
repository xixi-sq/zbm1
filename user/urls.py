from django.conf.urls import url

from user import apis

urlpatterns = [
    url(r'^test/',apis.test),
    url(r'^login/',apis.login),

    # url(r'^register/',apis.register),



]