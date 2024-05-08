from django.db import models

# Create your models here.
from datetime import datetime


class Vendor_details(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(max_length=100,primary_key=True)
    # on_time_delivery_rate=models.FloatField()

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor_details, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

    def __str__(self):
        return f"Performance for {self.vendor.name} on {self.date}"
