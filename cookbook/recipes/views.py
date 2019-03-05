from django.shortcuts import render, redirect
from .models import Category, Recipe, Review, Ingredient, Step, Profile
from .forms import RegistrationForm, RecipeForm, ReviewForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q

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

@login_required
def recipe_create(request):
    # Add new recipe.
    context = {}
    context['form'] = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False)
            x.picture = request.FILES['picture']
            x.added_by = User.objects.get(username=request.user)
            x.save()
            return redirect('recipes:home') # Change it back to selected detail page.
        else:
            context['form'] = form
            return render(request, 'test.html', context)
    else:
        return render(request, 'test.html', context)

@login_required
def recipe_list(request):
    # use paginator here.
    # from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    pass

@login_required
def recipe_detail(request, recipe_id):
    # Recipe details
    context = {}
    context['recipe'] = Recipe.objects.get(id=recipe_id)
    context['reviews'] = Review.objects.all().filter(~Q(user=request.user), recipe=recipe_id) # Show reviews except the current user's.
    context['my_review'] = Review.objects.get(user=request.user, recipe=recipe_id) # Show the review of the current user.
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
    pass

@login_required
def review(request, recipe_id):
    # With rating and comment.
    pass

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
def user_detail(request, user_id):
    # Userinfo.
    pass

@login_required
def user_update(request, user_id):
    context = {}
    pass

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
            print('hi')
            
    return render(request, 'login.html', context)

def user_logout(request):
    context = {}
    logout(request)
    return redirect('recipes:index')