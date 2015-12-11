from rest_framework import serializers, fields


class SearchResultSerializer(serializers.Serializer):
    content_type = fields.CharField(source='model_name')
    name = fields.SerializerMethodField()
    description = fields.SerializerMethodField()
    thumbnail = fields.SerializerMethodField()
    webpage = fields.SerializerMethodField()
    url = fields.SerializerMethodField()
    



