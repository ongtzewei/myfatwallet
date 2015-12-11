from api.models import Wallet
from api.serializers import SimpleUserSerializer
from rest_framework import serializers


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='wallet-detail',lookup_field='pk')
    class Meta:
        model = Wallet

    def get_owner(self, obj):
        return obj.owner.username


class SimpleWalletSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta:
        model = Wallet
    
    def get_owner(self, obj):
        return obj.owner.username
