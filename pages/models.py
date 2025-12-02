from django.db import models
from django.utils import timezone

# Create your models here.

class ConversionHistory(models.Model):

    category = models.CharField(max_length=50)
    targetUnit = models.CharField(max_length=50)
    convertUnit = models.CharField(max_length=50)
    amount = models.FloatField()
    result = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
 

    def __str__(self):
        return f'{self.category} - {self.targetUnit}'