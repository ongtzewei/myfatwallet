from api.models import Merchant
from api.serializers import SimpleMerchantSerializer
from rest_framework import generics, permissions


class MerchantList(generics.ListAPIView):
    '''
    Retrieves the list of merchants
    '''
    queryset = Merchant.objects.all()
    serializer_class = SimpleMerchantSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MerchantDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieves the details for a specific merchant
    '''
    queryset = Merchant.objects.all()
    serializer_class = SimpleMerchantSerializer
    permission_classes = (permissions.IsAuthenticated,)

