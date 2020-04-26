from rest_framework import routers
from django.urls import path

from .api import (
    ItemViewSet,
    OrderItemViewSet,
    add_to_cart
)

router = routers.DefaultRouter()

router.register('api/items', ItemViewSet, 'items')
router.register('api/orderitems', OrderItemViewSet, 'orderitems')


urlpatterns = [
    path('api/add-to-cart/<slug>', add_to_cart, name="add-to-cart")
]

urlpatterns += router.urls
