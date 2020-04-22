from commerce.models import Item
from rest_framework import viewsets, permissions
from .serializers import ItemSerializer

# Item Viewset -> allows
from rest_framework.views import APIView
from rest_framework.response import Response


class ItemViewSet(viewsets.ModelViewSet):

    # permission_classes = [
    # permissions.IsAuthenticated
    # ]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # def get_queryset(self, request, format=None):
    #items = [item for item in Items.objects.all()]
    # return Response(items)


'''
#need to register in urls.py 

class ListItems(APIView):
    def get(self, request, format=None):
        items = [item for item in Items.objects.all()]
        return Response(items)

    @classmethod
    def get_extra_actions(cls):
        return []
'''
