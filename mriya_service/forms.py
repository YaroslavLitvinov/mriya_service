from django import forms
from mriya_service.models import MyQuery, Config

class QueryForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput(), required=True)
    query = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))
    class Meta:
        model = MyQuery
        fields = ['query', 'user']

    def __init__(self,
                 dst_choices=[('BAD', 'DATA')],
                 src_choices=[('BAD', 'DATA')], *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['src'] = forms.ChoiceField(choices=src_choices)
        self.fields['dst'] = forms.ChoiceField(choices=dst_choices)

class ConfigForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput(), required=True)
    config = forms.FileField(required=False)
    class Meta:
        model = Config
        fields = ['config', 'user']
