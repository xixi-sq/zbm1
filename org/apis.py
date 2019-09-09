from django.shortcuts import render

from libs.http import render_json
from org import forms
from org.forms import OrgForm


# Create your views here.
from org.models import Org


def set_org(request):
    '''新增组织'''
    orgForm = forms.OrgForm(request.POST)

    if not orgForm.is_valid():
        return render_json(code=0,message='org信息填写不正确')

    #获取
    # print(orgForm.cleaned_data)

    #保存
    org = orgForm.save()

    return render_json(code=1,data=orgForm.cleaned_data,message='org录入成功')
