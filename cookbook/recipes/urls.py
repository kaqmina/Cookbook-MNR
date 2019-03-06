from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.user_create, name='register'),
    path('recipe/create', views.recipe_create, name='create_recipe'),
    path('account/', views.user_detail, name='user_detail'),
    path('account/edit', views.user_update, name='user_update'),
    path('home', views.home, name='home'),
    path('<int:recipe_id>/detail', views.recipe_detail, name='detail'),
    path('<int:recipe_id>/review', views.review, name='review'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]