from django.contrib import admin
from home.models import Contact
from .models import *


# password=we3@smp123
# Register your models here.
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


