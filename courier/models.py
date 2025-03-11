from django.db import models

# Create your models here.
class Courier(models.Model):
    product_provider_name = models.CharField(max_length=100)
    product_receiver_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    p_weight_in_kg = models.IntegerField()
    product_location = models.CharField(max_length=15)

    