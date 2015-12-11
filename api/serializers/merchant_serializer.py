from api.models import Merchant
from api.serializers import SimpleInventorySerializer
from rest_framework import serializers


class SimpleMerchantSerializer(serializers.ModelSerializer):
    inventory_stock = SimpleInventorySerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='merchant-detail',lookup_field='pk')
    class Meta:
        model = Merchant
        fields = ('name','code','address','inventory_stock', 'url')
