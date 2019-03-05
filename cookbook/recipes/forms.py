from django.forms import ModelForm
from .models import Recipe, Review, Profile, Ingredient, Step
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

# What to fix:
# TimeField widget.
# - Instead of TextInput, use a more appropriate one.

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput()
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        # fields = '__all__'
        exclude = ['added_by','date_added', 'is_archived']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ['user', 'date_reviewed', 'recipe']