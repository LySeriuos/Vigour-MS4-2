from django.db import models
# the category model which will give our products a category
# like clothing, kitchen and dining, or deals.
# null equals true and blank equals true so that the friendly name is optional.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    subcategory = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_subcategory(self):
        return self.subcategory


# null=True, blank=True this gives us option to use products which do not have
# some of the categories or the values is empty

# on_delete=models.SET_NULL it gives option to make empty that category
# in database rather than deleting product.


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    highlight = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    list1 = models.CharField(max_length=254, null=True, blank=True)
    list2 = models.CharField(max_length=254, null=True, blank=True)
    list3 = models.CharField(max_length=254, null=True, blank=True)
    list4 = models.CharField(max_length=254, null=True, blank=True)
    daily_dose = models.CharField(max_length=254, null=True, blank=True)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    subcategory = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

# use 'python3 manage.py makemigrations --dry-run'
# to find if there are any issues in the project before making changes
# use python3 manage.py migrate --plan to see which migrations going to be
