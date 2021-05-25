from django.shortcuts import render, redirect
from dashboard.models import Home, Client, Products, Reference, Recipes,Register
from django.utils import timezone
import datetime


def home(request):
    posts = Home.objects.all()
    clients = Client.objects.all()
    recipes = Recipes.objects.all()
    abouts = Products.objects.all().order_by("-price")[3:]
    blogs = Products.objects.all().order_by("-price")[:3]

    ctx = {
        "posts": posts,
        "recipes": recipes,
        "clients": clients,
        "abouts": abouts,
        "blogs": blogs,
    }
    return render(request, 'store/index.html', ctx)


def recipe(request):
    recipes = Recipes.objects.all()
    ctx = {
        "recipes": recipes,
    }
    return render(request, 'store/recipe.html', ctx)


def about(request):
    abouts = Products.objects.all().order_by("-price")[3:]
    ctx = {
        "abouts": abouts,
    }
    return render(request, 'store/about.html', ctx)


def blog(request):
    blogs = Products.objects.all().order_by("-price")[:3]
    ctx = {

        "blogs": blogs,
    }
    return render(request, 'store/blog.html', ctx)


def contact(request):
    return render(request, 'store/contact.html')

def register(request):
    register = Register()
    if request.POST:
        register.name = request.POST.get("name")
        register.email = request.POST.get("email")
        register.password = request.POST.get("phone")
        register.save()

    return render(request, 'store/register.html')

def footer(request):
    reference = Reference()
    if request.POST:
        reference.name = request.POST.get("name")
        reference.email = request.POST.get("email")
        reference.phone = request.POST.get("phone")
        reference.message = request.POST.get("message")
        reference.save()

    return render(request, 'footer.html')
