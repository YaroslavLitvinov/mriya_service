from django import forms
from mriya_service.models import MyQuery
from mriya_service.models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['user']

class QueryForm(forms.ModelForm):
    query = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))
    class Meta:
        model = MyQuery
        fields = ['query']



