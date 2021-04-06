from django.shortcuts import render
from products.models import *

def sweets(request):
    torts_images = products_images_phones = ProductImage.objects.filter(is_active = True, is_main = True, product__category__id = 1)
    return render(request, 'categories/sweets.html', locals())

def mousse(request):
    torts_images = products_images_phones = ProductImage.objects.filter(is_active = True, is_main = True, product__category__id = 3)
    return render(request, 'categories/mousse cakes.html', locals())

def product(request, product_id):
    product = Product.objects.get(id = product_id)

    return render(request, 'products/product.html', locals())
def sponge(request):
    torts_images = products_images_phones = ProductImage.objects.filter(is_active = True, is_main = True, product__category__id = 2)
    return render(request, 'categories/sponge cakes.html', locals())