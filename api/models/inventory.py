import hashlib
import os
import uuid
from django.db import models
from time import time


def image_upload_path(instance, filename):
    # creating a path from an incoming image file uploaded using either the model's primary key or uuid field to generate a random hash string
    # <base folder for user uploads>/<django model object for image>/<a-zA-Z0-9>/<a-zA-Z0-9>/<a-zA-Z0-9>/filename
    # examples:
    # uploads/recipes/e3/2S/23/b655f20638017e6306fd1ca8cc9244d3.jpg.jpg
    # uploads/foodblogs/r6/Fd/12/c4867143cd7159fdf2092fb774720715.jpg
    (file_name, file_ext) = os.path.splitext(filename)
    strclass = str(instance.__class__.__name__).lower()
    
    instance_id = hasattr(instance, 'id') and instance.id or None
    if not bool(instance_id): raise Exception('Upload failed due to missing model id')
    
    strtime = str(time())
    strpk = str(instance_id)
    hashed_path = hashlib.md5(strpk).hexdigest()
    hashed_name = hashlib.md5(strpk+strtime).hexdigest()
    hashed_name = ''.join([hashed_name, file_ext])
    return os.path.normpath(os.path.join(strclass, hashed_path[0:2], hashed_path[2:4], hashed_path[4:6], hashed_name))


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_upload_path)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    original_price = models.DecimalField(max_digits=5, decimal_places=2)
    reduced_price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.TextField(null=True, blank=True)
    class Meta:
        app_label = 'api'
        db_table = 'api_inventory'
    
    def __unicode__(self):
        return u'%s has been reduced from %s to %s' %(self.name, self.original_price, self.reduced_price)
