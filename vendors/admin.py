from django.contrib import admin

# Register your models here.
from .models import Vendor_details,HistoricalPerformance

admin.site.register(Vendor_details)
admin.site.register(HistoricalPerformance)


from django.apps import AppConfig
from po.models import PurchaseOrder
from .signals import update_historical_performance_on_completion

class MyAppConfig(AppConfig):
    name = 'vendors'  # Replace with your app's name

    def ready(self):
        super().ready()
        update_historical_performance_on_completion.connect(sender=PurchaseOrder)
