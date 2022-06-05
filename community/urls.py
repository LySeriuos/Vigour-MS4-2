from django.urls import path
from . import views


urlpatterns = [
    path('our_trainers/', views.community, name='community'),
    ]
