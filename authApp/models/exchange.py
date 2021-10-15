from django.db import models
from .product import Product
from .user import User
from datetime import datetime

class Exchange(models.Model):
    exch_id = models.AutoField(primary_key=True)
    exch_userorigin_id = models.ForeignKey(User, related_name='exch_userorigin', on_delete=models.CASCADE)
    exch_userdestination_id = models.ForeignKey(User, related_name='exch_userdestination', on_delete=models.CASCADE)
    exch_prod_id = models.ForeignKey(Product, related_name='exch_prod', on_delete=models.CASCADE)
    exch_fecha = models.DateTimeField(default=datetime.now)



