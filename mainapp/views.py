from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
import random

# Create your views here.
def get_basket(request):
    if request.user.is_authenticated:
        return Basket.objects.filter(user=request.user)

def get_hot_product():
    products = Product.objects.filter(is_active=True, category__is_active=True)
    return random.choice(list(products))

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)
    return same_products


def index(request):
    context = {
        'title': 'Virtual shop',
        'add_title': 'Main page',
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request, category_pk=None):
    print(category_pk)
    title = 'Catalog'
    categories = ProductCategory.objects.filter(is_active=True)
    products = Product.objects.all()


    if category_pk:
        if category_pk == '0':
            category = {'name': 'все'}
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('name')
        else:
            category = get_object_or_404(ProductCategory, pk=category_pk)
            products = Product.objects.filter(category__pk=category_pk, is_active=True).order_by('name')

        content = {
            'title': title,
            'categories': categories,
            'category': category,
            'products': products,
            'basket': get_basket(request),
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'title': title,
        # 'products': products,
        'hot_product': hot_product,
        'same_products': same_products,
        'categories': categories,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/catalog.html', context)

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
        'categories': Product.objects.all(),
        'category': product.category,
        'basket': get_basket(request),
    }
    render_list = {
        'Oculus rift': 'OculusRift.html',
        'Playstation VR': 'PSVR.html',
        'HTC Vive': 'HTC_VIVE.html',
        'Holo Lens': 'halolens.html',
    }

    if product.name in render_list:
        return render(request, 'mainapp/' + render_list[product.name], context)
    else:
        return render(request, 'mainapp/product.html', context)


def halolens(request):
    context = {
        'title': 'Holo lens',
    }
    return render(request, 'mainapp/halolens.html', context)


def htc_vive(request):
    context = {
        'title': 'HTC Vive',
    }
    return render(request, 'mainapp/HTC_VIVE.html', context)


def oculus_rift(request):
    context = {
        'title': 'Oculus rift',
    }
    return render(request, 'mainapp/OculusRift.html', context)


def psvr(request):
    context = {
        'title': 'PSVR',
    }
    return render(request, 'mainapp/PSVR.html', context)


def contacts(request):
    contact = [
        {'phone': '+7 (495) 999 88 77',
         'email': 'info@virtualreality.ru',
         'address': 'Малый Толмачевский переулок, дом 8'},
    ]

    context = {
        'title': 'Contacts',
        'contacts': contact,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/Contacts.html', context)

