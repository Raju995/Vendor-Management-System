from django.db import models

# Create your models here.
from datetime import datetime
from vendors.models import Vendor_details  # Assuming the Vendor model is in a 'vendors' app

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, primary_key=True)  # Primary Key
    vendor_no= models.ForeignKey(Vendor_details, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField(default="")
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50,choices=[
      ('pending', 'Pending'),
      ('completed', 'Completed'),
      ('cancelled', 'Cancelled'),
         ],default="Pending")
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    acknowledgment_status=models.CharField(max_length=10,choices=[('yes', 'Yes'),('no', 'No')],default="No")
