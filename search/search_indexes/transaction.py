from api.models import Transaction
from haystack import indexes


class TransactionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    description = indexes.CharField(model_attr='description',null=True)
    category = indexes.CharField(model_attr='category',null=True)
    date_added = indexes.DateTimeField(model_attr='date_added')
    last_modified = indexes.DateTimeField(model_attr='last_modified')
    
    def get_model(self):
        return Transaction

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
