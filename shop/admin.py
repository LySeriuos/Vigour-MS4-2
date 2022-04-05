from django.contrib import admin
from .models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # The tuple that will tell the admin which fields to display.
    list_display = (
        'sku',
        'name',
        'category',
        'subcategory',
        'price',
        'rating',
        'image'
    )
# sorting products by:

    ordering = (
        'sku',
        'subcategory',
        'category'
        )


# to change the order of the columns in the admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


# use this to load data python3 loaddata categories
# start with categories since the products
# need to know which category to go in.
