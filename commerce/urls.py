from rest_framework import routers
#from .api import ListItems
from .api import ItemViewSet, OrderItemViewSet

router = routers.DefaultRouter()

router.register('api/items', ItemViewSet, 'items')
router.register('api/orderitems', OrderItemViewSet, 'orderitems')

urlpatterns = router.urls
