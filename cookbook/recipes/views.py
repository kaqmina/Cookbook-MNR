from django.shortcuts import render, redirect
from .models import Category, Recipe, Review
from .forms import RegistrationModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group

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
    # Home page.
    context = {}
    return render(request, 'home.html', context)

@login_required
def recipe_create(request):
    # Add new recipe.
    pass

@login_required
def recipe_detail(request, recipe_id):
    # Recipe details
    pass

@login_required
def recipe_update(request, recipe_id):
    # Update details.
    pass

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
    form = RegistrationModelForm()
    context = {}
    if request.user.is_authenticated:
        return redirect('recipes:home')
    
    context['form'] = form
    if request.method == 'POST':
        form = RegistrationModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password'])
            user.save()
            # Add user to NormalUser group. | For permission testing.
            g = Group.objects.get(name='NormalUser')
            g.user_set.add(user)
            login(request, user)
            return redirect('recipes:home')
        else:
            context['form'] = form
            return redirect('recipes:index')
    return render(request, 'registration.html', context)

@login_required
def user_detail(request, user_id):
    # Userinfo.
    pass

@login_required
def user_update(request, user_id):
    # Update details.
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