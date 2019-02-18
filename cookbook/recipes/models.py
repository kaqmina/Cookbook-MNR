from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    related_name='cat', blank=False, null=False)
    date_added = models.DateTimeField(default=dt.now())

    def __str__(self):
        return '{}'.format(self.name)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='rec')
    date_reviewed = models.DateTimeFied(default=dt.now())

    def __str__(self):
        return '{}'.format(self.recipe)
