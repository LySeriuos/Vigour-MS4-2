from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<product_id>', views.product_detail_view, name='product_detail'),
]
