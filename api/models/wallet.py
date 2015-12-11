from django.conf import settings
from django.db import models


class Wallet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner_wallet')
    transactions = models.ManyToManyField('api.Transaction',blank=True)
    class Meta:
        app_label = 'api'
        db_table = 'api_wallet'
    
    def __unicode__(self):
        return u'Wallet belonging to %s' %(self.owner)
