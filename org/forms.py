from django import forms

from org.models import Org, Building


class OrgForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = '__all__'


class BuildingFrom(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'
