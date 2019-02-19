from django.forms import ModelForm
from .models import Recipe, Review
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

class RegistrationModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput()
        }