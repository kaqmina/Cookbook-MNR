from django.shortcuts import render

# Create your views here.
def index(request):
    # Home page.
    context = {}
    return render(request, 'index.html', context)

@login_required
def category_create(request):
    # Category: Dessert, Appetizer, etc. (Max. 4)
    pass

@login_required
def category_update(request, category_id):
    # Update details.
    pass

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
    pass

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
    pass

def user_logout(request):
    pass