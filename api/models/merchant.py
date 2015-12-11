from django.db import models


class Merchant(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=12)
    address = models.TextField()
    inventory_stock = models.ManyToManyField('api.Inventory', blank=True)
    class Meta:
        app_label = 'api'
        db_table = 'api_merchant'
    
    def __unicode__(self):
        return u'Merchant Code for %s: %s' %(self.name, self.code)
