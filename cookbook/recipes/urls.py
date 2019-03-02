from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.user_create, name='register'),
    path('create/', views.recipe_create, name='create_recipe'),
    path('home', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]