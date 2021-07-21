from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index,name='home'),
    path("home", views.index,name='home'),
    path("about", views.about,name='about'),
    path("service", views.service,name='service'),
    path("contact", views.contact,name='contact'),
    path("cart/", views.cart,name='cart'),
    path("update_item/", views.updateItem,name="update_item"),
    path("process_order/", views.processOrder,name="process_order"),
]
