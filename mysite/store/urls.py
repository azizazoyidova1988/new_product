from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/', views.recipe, name="recipe"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name="register"),
    path('footer/', views.footer, name="footer"),
    path('dashboard/', include('dashboard.urls')),

]