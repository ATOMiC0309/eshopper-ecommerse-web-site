from django.shortcuts import render, redirect

from .models import Category, Subcategory, Product
from .forms import ProductForm


# Create your views here.
def index(request):
    context = {
        'categories': Category.objects.raw('''SELECT * FROM shop_category'''),
        'subcategories': Subcategory.objects.all(),
        'products': Product.objects.all()
    }

    return render(request, 'shop/index.html', context=context)


def shop(request):
    context = {
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
        'products': Product.objects.all(),
        'product_count': Product.objects.count(),
    }

    return render(request, 'shop/shop.html', context=context)


def product_by_category(request, category_pk):
    category = Subcategory.objects.get(pk=category_pk)
    context = {
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
        'products': Product.objects.filter(category=category),
        'product_count': Product.objects.count(),
    }

    return render(request, 'shop/shop.html', context=context)


def detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    product.views += 1
    product.save()
    context = {
        'product': product,
        'products': Product.objects.all(),
    }
    return render(request, 'shop/detail.html', context)


def filter_by(request, filter_key):
    context = {
        'categories': Category.objects.all(),
        'subcategories': Subcategory.objects.all(),
        'product_count': Product.objects.count(),
    }
    if filter_key == 'last':
        context['products'] = Product.objects.filter(name=Product.objects.first())
        print(context['products'], "*" * 40)
    elif filter_key == 'first':
        context['products'] = Product.objects.filter(name=Product.objects.last())
    else:
        context['products'] = Product.objects.order_by(filter_key).reverse()

    return render(request, 'shop/shop.html', context=context)


def product_update(request, pk):
    """for  Recipe update(change)"""

    product = Product.objects.get(pk=pk)

    product_form = ProductForm(data=request.POST or None, instance=product, files=request.FILES or None)
    if product_form.is_valid():
        product_form.save()
        return detail(request, pk)

    context = {
        'product_form': product_form,
    }
    return render(request, 'shop/product_form.html', context=context)


def product_delete(request, pk):
    """for product delete"""

    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('index')

    return render(request, 'shop/product_delete.html', {"product": product})