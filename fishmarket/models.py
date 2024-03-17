from django.db import models

class FishMarketModel(models.Model):
    weight = models.FloatField(null=False, blank=False)
    length1 = models.FloatField(null=False, blank=False)
    length2 = models.FloatField(null=False, blank=False)
    length3 = models.FloatField(null=False, blank=False)
    height = models.FloatField(null=False, blank=False)
    width = models.FloatField(null=False, blank=False)
