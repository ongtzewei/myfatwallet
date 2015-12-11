from api.serializers import SimpleUserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions


class UserList(generics.ListAPIView):
    '''
    Retrieves the list of active users
    '''
    queryset = User.objects.all()
    serializer_class = SimpleUserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieves the details for an active user
    '''
    queryset = User.objects.all()
    serializer_class = SimpleUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

