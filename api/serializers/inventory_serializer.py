from api.models import Inventory
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail


class SimpleInventorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='inventory-detail',lookup_field='pk')
    class Meta:
        model = Inventory
        fields = ('pk', 'name','image','original_price','reduced_price', 'ingredients', 'url')
    
    def get_image(self, obj):
        return get_thumbnail(obj.image, '320x210', crop='center', quality=99).url
