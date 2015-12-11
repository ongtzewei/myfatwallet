from api.models import Wallet
from api.serializers import WalletSerializer, SimpleWalletSerializer
from rest_framework import generics, permissions


class WalletList(generics.ListAPIView):
    '''
    Retrieves the list of active wallets
    '''
    queryset = Wallet.objects.filter(owner__is_active=True)
    serializer_class = SimpleWalletSerializer
    permission_classes = (permissions.IsAuthenticated,)


class WalletDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieves the details for an active wallet
    '''
    queryset = Wallet.objects.filter(owner__is_active=True)
    serializer_class = WalletSerializer
    permission_classes = (permissions.IsAuthenticated,)

