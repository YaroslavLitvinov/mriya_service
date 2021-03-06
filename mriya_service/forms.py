from django import forms
from mriya_service.models import MyQuery, Config
from elfinder.fields import ElfinderFormField

DEFAULT_CHOICE = [(0, 'BAD DATA')]

class QueryForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput(), required=True)
    hidden_filename = forms.CharField(widget=forms.HiddenInput(), required=False)
    filename = ElfinderFormField(optionset='default', start_path=None)
    flist = forms.CharField(widget=forms.SelectMultiple(), required=True)
    query = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))
    src = forms.ChoiceField(choices=DEFAULT_CHOICE)
    dst = forms.ChoiceField(choices=DEFAULT_CHOICE)
    class Meta:
        model = MyQuery
        fields = ['query', 'user', 'src', 'dst', 'filename']

    def set_choices(self, choices):
        self.fields['src']._set_choices(choices)
        self.fields['dst']._set_choices(choices)

class ConfigForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput(), required=True)
    config = forms.FileField(required=False)
    class Meta:
        model = Config
        fields = ['config', 'user']
