
from rest_framework import serializers 
from .models import Vendor_details,HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_details
        fields = ['name', 'contact_details', 'address', 'vendor_code']

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = ["vendor","date","on_time_delivery_rate","quality_rating_avg","average_response_time","fulfillment_rate"]