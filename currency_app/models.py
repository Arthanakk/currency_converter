from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Currency_detail(models.Model):
    amount = models.FloatField()
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    converted_amount = models.FloatField()
    converstion_rate =models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.amount} {self.from_currency} to {self.to_currency}"

