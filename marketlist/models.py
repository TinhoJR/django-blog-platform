from django.db import models

# Create your models here.

class MarketList(models.Model):

    item = models.CharField(max_length=250)
    qty = models.IntegerField()
    price = models.IntegerField()
    

    @property  
    def total(self):
        return self.price * self.qty

    def __str__(self):
        return f"{self.item} - {self.qty}" 

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save() 

