from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from product.models import Product, Comment, Rating, Order
from product.forms import CommentForm, CommentModelForm, RatingModelForm, OrderCreateForm


class ProductView(ListView):

    def get(self, *args, **kwargs):
        print('GET', args, kwargs)


def home_page(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)


def detail_page(request, product_id):
    ratings = Rating.objects.filter(product=product_id).order_by('-created_at').all()
    context = {
        'product': Product.objects.get(id=product_id),
        'comments': Comment.objects.filter(product=product_id).order_by('-id').all(),
        'rating': round(sum([int(x.point) for x in ratings]) / (len(ratings) or 1), 2),
        'comment_form': CommentModelForm(),
        'rating_form': RatingModelForm(),
        'is_authenticated': request.user.is_authenticated,
        'user': request.user
    }
    return render(request, 'detail.html', context)


def comment_views(request, product_id):
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                text=form.data['text'],
                product_id=product_id
            )
        return redirect(request.headers.get('Referer'))


def rating_views(request, product_id):
    if request.method == 'POST':
        form = RatingModelForm(request.POST)
        if form.is_valid():
            Rating.objects.create(
                user=request.user,
                point=form.data['point'],
                product_id=product_id
            )
    return redirect(request.headers.get('Referer'))


def order_create(request, product_id):
    if request.method == 'GET':
        form = OrderCreateForm()
        if form.is_valid():
            form.save()
        return render(request, 'order.html', context={'order_form': form,
                                                       'product': product_id
                                                       })
    if request.method == 'POST':
        form = OrderCreateForm()
        if form.is_valid():
            form.save()
    return render(request, 'index.html', context={'order_form': form,
                                                  'product': product_id
                                                  })