"""OnlineStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from OnlineStore import settings
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home',),
    path('detail/<int:product_id>', views.detail_page, name='detail'),
    path('comment/<int:product_id>', views.comment_views, name='comment'),
    path('rating/<int:product_id>', views.rating_views, name='rating'),
    path('orders/<int:product_id>', views.order_create, name='order_create'),

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, }),
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
    re_path(r'^rating/(?P<product_id>.*)$', serve,)
]
