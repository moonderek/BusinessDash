from rest_framework import routers
#from .api import ListItems
from .api import ItemViewSet

router = routers.DefaultRouter()

router.register('api/items', ItemViewSet, 'items')
#router.register('api/items', ListItems, 'items')

urlpatterns = router.urls
