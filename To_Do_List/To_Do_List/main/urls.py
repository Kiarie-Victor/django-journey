from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('home/add-items', views.add_items, name='add_items'),
]
