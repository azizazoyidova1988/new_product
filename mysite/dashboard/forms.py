from django import forms
from .models import Home, Products,Client,Reference,Recipes,Register


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = "__all__"
        labels={
            "name":"Enter name"
        }

class ProductsForm(forms.ModelForm):
    class Meta:
        model =Products
        fields = "__all__"
        labels={
            "name":"Enter name"
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        labels={
            "name":"Enter name"
        }

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = "__all__"
        labels={
            "name":"Enter name"
        }

class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = "__all__"
        labels={
            "name":"Enter name"
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
        labels={
            "name":"Enter name"
        }