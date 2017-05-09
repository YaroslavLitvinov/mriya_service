from django import forms
from mriya_service.models import MyQuery

class QueryForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput(), required=True)
    query = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))
    class Meta:
        model = MyQuery
        fields = ['query', 'user']
