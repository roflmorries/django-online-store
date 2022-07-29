from django.shortcuts import render
from product.models import Product


def home_page(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)


def detail_page(request, product_id):
    context = {
        'products': Product.objects.filter(id=product_id)
    }
    return render(request, 'detail.html', context)