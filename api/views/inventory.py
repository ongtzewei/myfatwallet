from api.models import Inventory
from api.serializers import SimpleInventorySerializer
from rest_framework import generics, permissions


class InventoryList(generics.ListAPIView):
    '''
    Retrieves the list of inventory items
    '''
    queryset = Inventory.objects.all()
    serializer_class = SimpleInventorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieves the details for a specific inventory item
    '''
    queryset = Inventory.objects.all()
    serializer_class = SimpleInventorySerializer
    permission_classes = (permissions.IsAuthenticated,)

