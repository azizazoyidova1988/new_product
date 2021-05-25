from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('home/list/', views.home_list, name="home_list"),
    path('home/add/', views.home_create, name="home_add"),
    path('home/<int:home_id>/edit/', views.home_edit, name="home_edit"),
    path('home/<int:home_id>/delete/', views.home_delete, name="home_delete"),

    path('client/list/', views.client_list, name="client_list"),
    path('client/add/', views.client_create, name="client_add"),
    path('client/<int:client_id>/edit/', views.client_edit, name="client_edit"),
    path('client/<int:client_id>/delete/', views.client_delete, name="client_delete"),

    path('product/list/', views.product_list, name="product_list"),
    path('product/add/', views.product_create, name="product_add"),
    path('product/<int:product_id>/edit/', views.product_edit, name="product_edit"),
    path('product/<int:product_id>/delete/', views.product_delete, name="product_delete"),

    path('reference/list/', views.reference_list, name="reference_list"),
    path('reference/add/', views.reference_create, name="reference_add"),
    path('reference/<int:reference_id>/edit/', views.reference_edit, name="reference_edit"),
    path('reference/<int:reference_id>/delete/', views.reference_delete, name="reference_delete"),

    path('recipe/list/', views.recipe_list, name="recipe_list"),
    path('recipe/add/', views.recipe_create, name="recipe_add"),
    path('recipe/<int:recipe_id>/edit/', views.recipe_edit, name="recipe_edit"),
    path('recipe/<int:recipe_id>/delete/', views.recipe_delete, name="recipe_delete"),

    path('register/list/', views.register_list, name="register_list"),
    path('register/add/', views.register_create, name="register_add"),
    path('register/<int:register_id>/edit/', views.register_edit, name="register_edit"),
    path('register/<int:register_id>/delete/', views.register_delete, name="register_delete")

]

