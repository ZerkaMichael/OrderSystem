from django.contrib import admin
from cart.models import Order, CartItem, OrderItem

from shop.models import Product

# Register your models here.

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
