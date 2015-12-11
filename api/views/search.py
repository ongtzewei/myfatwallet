import re
from api.models import Transaction, Wallet
from api.serializers.searchresult_serializer import SearchResultSerializer
from haystack.inputs import Raw
from haystack.query import EmptySearchQuerySet, SearchQuerySet, SQ
from rest_framework import permissions, mixins, viewsets


class SearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SearchResultSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self, *args, **kwargs):
        models = (Transaction, Wallet)
        sq = SQ()
        request = self.request
        results = EmptySearchQuerySet()
        
        if 'query' in request.GET:
            for token in re.findall(r'[\w]+', request.GET['query']):
                sq |= SQ(content=token)
            sq |= SQ(content=request.GET['query'])
            results = SearchQuerySet().models(*models).filter(sq).exclude(group=Raw('[* TO *]'))
        return results
