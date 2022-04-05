from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)

# use this to load data python3 loaddata categories
# start with categories since the products
# need to know which category to go in.
