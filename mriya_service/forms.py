from django.forms import ModelForm
from mriya_service.models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['user']
