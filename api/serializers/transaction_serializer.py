from api.models import Transaction
from rest_framework import serializers


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='transaction-detail',lookup_field='pk')
    class Meta:
        model = Transaction


class SimpleTransactionSerializer(serializers.HyperlinkedModelSerializer):
    cover = serializers.SerializerMethodField()
    class Meta:
        model = Transaction

