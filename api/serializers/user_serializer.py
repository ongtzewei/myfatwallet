from django.contrib.auth import get_user_model
from rest_framework import serializers


class SimpleUserSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='user-detail',lookup_field='pk')
    class Meta:
        model = get_user_model()
        fields = ('username','first_name','last_name','email', 'last_login')
