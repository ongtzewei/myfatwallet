from api.models import Transaction
from api.serializers import TransactionSerializer, SimpleTransactionSerializer
from rest_framework import generics, permissions


class TransactionList(generics.ListAPIView):
    '''
    Retrieves the list of transactions
    '''
    queryset = Transaction.objects.all()
    serializer_class = SimpleTransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieves the details for a transaction
    '''
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

