from django.contrib import admin
from .models import Profile, Category, Recipe, Review, Step, Ingredient

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Step)
admin.site.register(Ingredient)