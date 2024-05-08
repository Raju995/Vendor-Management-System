from rest_framework import serializers
from .models import PurchaseOrder
from vendors.serializer import VendorSerializer  # Assuming vendor_app has a VendorSerializer

class PurchaseOrderSerializer(serializers.ModelSerializer):
  vendor = VendorSerializer(read_only=True)  # Serialize vendor details

  class Meta:
    model = PurchaseOrder
    fields ='__all__'

class PurchaseOrderListSerializer(serializers.ModelSerializer):
  vendor_code = serializers.CharField(source='vendors.vendor_no', read_only=True)  # Include vendor name

  class Meta:
    model = PurchaseOrder
    fields = ['po_number','vendor_code']

class Acknowledge(serializers.ModelSerializer):
  vendor_code = serializers.CharField(source='vendors.vendor_no', read_only=True)  # Include vendor name


  class Meta:
    model=PurchaseOrder
    fields=['po_number','vendor_code',"acknowledgment_status"]