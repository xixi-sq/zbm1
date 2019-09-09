from django.conf.urls import url

from org import apis

urlpatterns = [
    url(r'^set_org/',apis.set_org)
]