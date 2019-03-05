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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput()
        }
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

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

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        exclude = ['date_added', 'recipe']

class StepForm(ModelForm):
    class Meta:
        model = Step
        exclude = ['date_added', 'recipe']