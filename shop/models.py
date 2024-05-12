from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "1. Categories"
        ordering = ["name"]


class Subcategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "2. Subcategories"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "3. Products"
        ordering = ["-pk"]
