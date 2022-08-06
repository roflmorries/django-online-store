from django.contrib import admin
from product.models import *
from product.models import Product


# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'updated_at', 'created_at']
    list_filter = ['id', 'title', 'description', 'price']
    search_fields = ['id', 'title', 'description', 'price', 'updated_at', 'created_at']


admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Order)
