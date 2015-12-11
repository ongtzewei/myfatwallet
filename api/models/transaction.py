from django.conf import settings
from django.db import models


class TransactionCategory(models.Model):
    label = models.CharField(max_length=32)
    sort = models.PositiveSmallIntegerField(default=10)
    class Meta:
        app_label = 'api'
        db_table = 'api_expenditure_category'
        ordering = ('sort',)
    
    def __unicode__(self):
        return u'%s' %(self.label)


class Transaction(models.Model):
    reference_no = models.CharField(max_length=20)
    payee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payee_transaction')
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(TransactionCategory)
    last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'api'
        db_table = 'api_transaction'
        ordering = ('date_created',)
    
    def __unicode__(self):
        return u'[%s] %s' %(self.category, self.description)

