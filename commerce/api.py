from commerce.models import Item
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse


from .serializers import ItemSerializer, OrderItemSerializer
from .models import Item, OrderItem, Order


class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return self.request.user.orderitems.all()


@api_view()
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )

    # get order that is not completed
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if order item is in order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            return JsonResponse({'Message': "The quantity was updated to your cart"})

        else:
            order.items.add(order_item)
            return JsonResponse({'Message': "This item was added to your cart"})

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)

        order.items.add(order_item)
        return JsonResponse({'Message': "This item was added to your cart"})


class ItemViewSet(viewsets.ModelViewSet):

    # permission_classes = [
    # permissions.IsAuthenticated
    # ]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# Secondary Method
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
