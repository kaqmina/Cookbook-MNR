from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# OneToOne Link User Profile | For additional information on the default User Model.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True)
    usertypes = (
        (True, 'Admin'),
        (False, 'User')
    )
    usertype = models.BooleanField(choices=usertypes, null=False, default=False)

    def __str__(self):
        return '{}'.format(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Category(models.Model):
    category = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.category)

# TimeField in forms: time_ = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='categories', null=True)
    date_added = models.DateTimeField(default=dt.now())
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    servings = models.IntegerField(validators=[MinValueValidator(0)], null=False, default=0)
    prep_time = models.DurationField()
    cook_time = models.DurationField()
    read_time = models.DurationField()
    picture = models.ImageField(upload_to='recipe_img', null=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(max_length=500)
    date_reviewed = models.DateTimeField(default=dt.now())
    
    def __str__(self):
        return 'User: {}, Recipe: {}'.format(self.user, self.recipe)

class Step(models.Model):
    # Step order will be determined by date added.
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps', null=False, blank=False)
    date_added = models.DateTimeField(default=dt.now())
    description = models.TextField()

    def __str__(self):
        return 'Recipe: {}, Step: {}'.format(self.recipe, self.description)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients', null=False, blank=False)
    date_added = models.DateTimeField(default=dt.now())
    ingredient = models.TextField()

    def __str__(self):
        return '{}'.format(self.ingredient)
    