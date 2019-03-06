from django.shortcuts import render, redirect
from .models import Category, Recipe, Review, Ingredient, Step, Profile
from .forms import RegistrationForm, UserForm, RecipeForm, ReviewForm, ProfileForm, IngredientForm, StepForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.forms.models import modelformset_factory
from django.forms import formset_factory
from django.db import IntegrityError, transaction

# Create your views here.
def index(request):
    # Index page.
    context = {}
    if request.user.is_authenticated:
        return redirect('recipes:home')
    else:
        return render(request, 'index.html', context)

@login_required
def home(request):
    # Home page. | Show trending, most popular, latest.
    context = {}
    context['latest_recipes'] = Recipe.objects.all().order_by('-id')[:4]
    return render(request, 'home.html', context)

# @login_required
# def recipe_create(request):
#     # Add new recipe.
#     context = {}
#     context['recipe_form'] = RecipeForm()
#     context['ingredients_form'] = IngredientForm()
#     context['step_form'] = StepForm()
#     if request.method == 'POST':
#         rec_form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             x = rec_form.save(commit=False)
#             x.picture = request.FILES['picture']
#             x.added_by = User.objects.get(username=request.user)
#             x.save()
#             return redirect('recipes:home') # Change it back to selected detail page.
#         else:
#             context['recipe_form'] = recipe_form
#             return render(request, 'create_recipe.html', context)
#     else:
#         return render(request, 'create_recipe.html', context)

@login_required
def recipe_create(request):
    # Add new recipe.
    context = {}
    # Formsets
    IngredientFormset = formset_factory(IngredientForm, extra=2)
    Ing_formset = IngredientFormset()
    StepFormset = formset_factory(StepForm, extra=2)
    Stp_formset = StepFormset()
    # Forms
    context['recipe_form'] = RecipeForm()
    context['ingredient_form'] = Ing_formset
    context['step_form'] = Stp_formset
    if request.method == 'POST':
        rec_form = RecipeForm(request.POST, request.FILES)
        formset_ing, formset_stp = \
            ing_formset(request.POST, prefix='fs1'), \
            stp_formset(request.POST, prefix='fs2')
        if rec_form.is_valid() and formset_ing.is_valid() and formset_stp.is_valid():
            x = rec_form.save(commit=False)
            x.picture = request.FILES['picture']
            x.added_by = User.objects.get(username=request.user)
            x.save()

            # Save formset values
            new_ingredients = []
            for ing_form in ing_formset:
                ingredient = ing_form.cleaned_data.get('ingredient')

                if ingredient:
                    new_ingredients.append(Ingredient(recipe=x, ingredient=ingredient))

            try:
                with transaction.atomic():
                    Ingredient.filter(recipe=x).delete()
                    Ingredient.objects.bulk_create(new_ingredients)
                    message.success(request, 'Added ingredients')
            except IntegrityError:
                messages.error(request, 'Error in ingredients')
                return redirect('recipes:home')

                
            new_steps = []
            for stp_form in stp_formset:
                step = ing_form.stp_form.get('step_desc')

                if ingredient:
                    new_steps.append(Step(recipe=x, description=step))
            try:
                with transaction.atomic():
                    Step.filter(recipe=x).delete()
                    Step.objects.bulk_create(new_steps)
                    message.success(request, 'Added steps')
            except IntegrityError:
                messages.error(request, 'Error in steps')
                return redirect('recipes:account')
        else:
            return render(request, 'create_recipe.html', context)
    else:
        return render(request, 'create_recipe.html', context)

def save_ingredient():
    pass

def save_steps():
    pass

@login_required
def recipe_list(request, category_id):
    # use paginator here.
    # from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    pass

@login_required
def recipe_detail(request, recipe_id):
    # Recipe details
    context = {}
    context['recipe'] = Recipe.objects.get(id=recipe_id)
    context['reviews'] = Review.objects.all().filter(~Q(user=request.user), recipe=recipe_id) # Show reviews except the current user's.
    try:
        context['my_review'] = Review.objects.get(user=request.user, recipe=recipe_id) # Show the review of the current user.
    except:
        context['my_review'] = False
    context['review'] = ReviewForm()    
    return render(request, 'detail.html', context)

@login_required
def recipe_update(request, recipe_id):
    # Update details.
    context = {}
    recipe = Recipe.object.get(id=recipe_id)
    context['recipe'] = recipe
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully updated.')
        else:
            context['form'] = form
            return render(request, 'test.html', context)
    else:
        context['form'] = RecipeForm(instance=recipe)
        return render(request, 'test.html', context)

@login_required
def recipe_delete(request, recipe_id):
    # Only set status to 0.
    context = {}
    pass

@login_required
def review(request, recipe_id):
    # With rating and comment.
    context = {}
    context['recipe_id'] = recipe_id
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.recipe_id = recipe_id
            x.user = User.objects.get(username=request.user)
            x.save()
            return redirect('recipes:detail', recipe_id)
        else:
            return redirect('recipes:detail', recipe_id)
    else:
        return redirect('recipes:detail', recipe_id)

def user_create(request):
    # Register user.
    form = RegistrationForm()
    context = {}
    if request.user.is_authenticated:
        return redirect('recipes:home')
    
    context['form'] = form
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('recipes:home')
        else:
            context['form'] = form
            return redirect('recipes:index')
    return render(request, 'registration.html', context)

@login_required
def user_profile(request):
    context = {}
    context['form'] = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.avatar = request.FILES['avatar']
            user.save()
            # Change redirected site.
            return redirect('recipes:home')
        else:
            context['form'] = form
            # Change
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)

@login_required
def user_detail(request):
    # Userinfo.
    context = {}
    context['profile'] = Profile.objects.get(user=request.user)

    context['my_recipes'] = Recipe.objects.all().filter(added_by=request.user)
    return render(request, 'account.html', context)

@login_required
def user_update(request):
    context = {}
    context['user_form'] = UserForm(instance=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            login(request, request.user)
            return redirect('recipes:user_detail')
        else:
            context['user_form'] = user_form
            return render(request, 'account_edit.html', context)
    else:
        context['form'] = UserForm(instance=request.user)
        return render(request, 'account_edit.html', context)

def user_login(request):
    # Login credentials.
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('recipes:index')
        else:
            print('User not found.')
            
    return render(request, 'login.html', context)

def user_logout(request):
    context = {}
    logout(request)
    return redirect('recipes:index')

def save_step(request):
    context = {}
    StepFormset = modelformset_factory(Step, StepForm)
    formset = StepFormset()
    context['step_formset'] = formset
    return render(request, 'test.html', context)