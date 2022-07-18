from django.shortcuts import render
from product.models import Product


def home(request):
    all_products = Product.objects.all()
    # all_categories=Category.objects.all()
    # request.session["all_categories"] = all_categories
    # return render_to_response('products/show_products.html',
    #                           {'all_products':all_products ,
    #                            'all_categories':all_categories,
    #                            'user':request.user})