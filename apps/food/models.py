from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.FloatField(default=0)

    def __str__(self):
        return f'Name {self.item_name}, $ {self.item_price:.2f}'