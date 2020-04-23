
# Register your models here.
from django.contrib import admin

from .models import Item, OrderItem

admin.site.register(Item)
admin.site.register(OrderItem)
