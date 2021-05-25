from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    full_name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Recipes(models.Model):
    title=models.CharField(max_length=250, blank=False,null=False)
    image = models.ImageField(upload_to="images/", blank=True, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=True, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.title


class Reference(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=45, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Register(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



