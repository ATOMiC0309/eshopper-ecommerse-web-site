from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Category, Subcategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created', 'published')
    list_display_links = ('pk', 'name')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'created', 'published')
    list_display_links = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'price', 'quantity', 'created', 'get_image')
    list_display_links = ('pk', 'name')

    def get_image(self, product):
        if product.image:
            res = mark_safe(
                f'<a href="{product.image.url}"  target="_blank"><img src="{product.image.url}" width="75px"/></a>')
        else:
            res = "No image"
        return res

    get_image.short_description = "Image"
