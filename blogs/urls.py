from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    # use 'int' otherwise 'add/' can be read as product id
    path('add/', views.add_blog, name='add_blog'),
    # path('<int:blog_id>/', views.edit_blog, name='blog_detail'),
    

]