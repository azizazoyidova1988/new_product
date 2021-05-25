from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Home, Client, Reference, Products, Recipes, Register
from .forms import ClientForm, ProductsForm, HomeForm, ReferenceForm, RegisterForm, RecipesForm
from . import services


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    products_count = services.get_products_count()
    clients_count = services.get_client_count()
    recipes_count = services.get_recipes_count()
    references_count = services.get_references_count()

    ctx = {

        "products_count": products_count,
        "clients_count": clients_count,
        "references_count": references_count,
        "recipes_count": recipes_count,

    }

    return render(request, 'dashboard/index.html', ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


def home_list(request):
    homes = services.get_homes()

    ctx = {
        "homes": homes
    }
    return render(request, 'dashboard/home/list.html', ctx)


def home_create(request):
    model = Home()
    form = HomeForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/home/form.html', ctx)


def home_edit(request, home_id):
    model = Home.objects.get(id=home_id)
    form = HomeForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/home/form.html', ctx)


def home_delete(request, home_id):
    model = Home.objects.get(id=home_id)
    model.delete()
    return redirect("home_list")


def client_list(request):
    clients = services.get_client()
    ctx = {
        "clients": clients
    }
    return render(request, 'dashboard/client/list.html', ctx)


def client_create(request):
    model = Client()
    form = ClientForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/client/form.html', ctx)


def client_edit(request, client_id):
    model = Client.objects.get(id=client_id)
    form = ClientForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('client_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/client/form.html', ctx)


def client_delete(request, client_id):
    model = Client.objects.get(id=client_id)
    model.delete()
    return redirect("client_list")


def product_list(request):
    products = services.get_product()
    print(products)
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)


def product_create(request):
    model = Products()
    form = ProductsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


def product_edit(request, product_id):
    model = Products.objects.get(id=product_id)
    form = ProductsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


def product_delete(request, product_id):
    model = Products.objects.get(id=product_id)
    model.delete()
    return redirect("product_list")


def recipe_list(request):
    recipes = services.get_recipes()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'dashboard/recipe/list.html', ctx)


def recipe_create(request):
    model = Recipes()
    form = RecipesForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/recipe/form.html', ctx)


def recipe_edit(request, recipe_id):
    model = Recipes.objects.get(id=recipe_id)
    form = ProductsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/recipe/form.html', ctx)


def recipe_delete(request, recipe_id):
    model = Recipes.objects.get(id=recipe_id)
    model.delete()
    return redirect("recipe_list")


def reference_list(request):
    references = services.get_references()
    ctx = {
        "references": references
    }
    return render(request, 'dashboard/reference/list.html', ctx)


def reference_create(request):
    model = Reference()
    form = ReferenceForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('reference_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/reference/form.html', ctx)


def reference_edit(request, reference_id):
    model = Reference.objects.get(id=reference_id)
    form = ReferenceForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('reference_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/reference/form.html', ctx)


def reference_delete(request, reference_id):
    model = Reference.objects.get(id=reference_id)
    model.delete()
    return redirect("reference_list")


def register_list(request):
    registers = services.get_references()
    ctx = {
        "registers": registers
    }
    return render(request, 'dashboard/register/list.html', ctx)


def register_create(request):
    model = Register()
    form = RegisterForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('register_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/register/form.html', ctx)


def register_edit(request, register_id):
    model = Register.objects.get(id=register_id)
    form = RegisterForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('register_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/register/form.html', ctx)


def register_delete(request, register_id):
    model = Register.objects.get(id=register_id)
    model.delete()
    return redirect("register_list")
