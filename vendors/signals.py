from django.db.models.signals import post_save
from django.dispatch import receiver
from po.models import PurchaseOrder
from .models import Vendor_details,HistoricalPerformance
from datetime import datetime
from django.db.models import Count, F

def calculate_on_time_delivery_rate(vendor):
    """
    Calculates the on-time delivery rate for a vendor.

    Args:
        vendor: The Vendor object for whom to calculate the rate.

    Returns:
        The on-time delivery rate as a float (0.0 to 1.0).
    """
    print("purchase  ",  PurchaseOrder.objects)
    completed_orders = PurchaseOrder.objects.filter(vendor_no=vendor, status='completed')
    # print("hus fus",completed_orders)
    # print("comp order",completed_orders)
    on_time_orders = completed_orders.filter(delivery_date__lte=F('delivery_date')) 
    # print("Ei dekh ans",len(on_time_orders) / len(completed_orders))
    return len(on_time_orders) / len(completed_orders) if completed_orders else 0.0
def calculate_quality_rating_avg(vendor):
    """
    Calculates the average quality rating for completed purchase orders of a vendor.

    Args:
        vendor: The Vendor object for whom to calculate the average.

    Returns:
        The average quality rating as a float, or None if no completed orders with ratings exist.
    """

    completed_orders = PurchaseOrder.objects.filter(vendor_no=vendor, status='completed', quality_rating__isnull=False)
    ratings = completed_orders.values_list('quality_rating', flat=True)
    # print("Cholche to?",sum(ratings) / len(ratings))
    return sum(ratings) / len(ratings) if ratings else None

def calculate_average_response_time(vendor):
    """
    Calculates the average response time for a vendor based on acknowledged purchase orders.

    Args:
        vendor: The Vendor object for whom to calculate the average response time.

    Returns:
        The average response time in days as a float, or None if no acknowledged orders exist.
    """

    acknowledged_orders = PurchaseOrder.objects.filter(vendor_no=vendor, acknowledgment_date__isnull=False)
    if not acknowledged_orders:
        return None

    response_times = [(order.acknowledgment_date - order.issue_date).total_seconds() / 86400 for order in acknowledged_orders]
    # print("berobi aj??",sum(response_times) / len(response_times))
    return sum(response_times) / len(response_times)

def calculate_fulfillment_rate(vendor):
    """
    Calculates the fulfillment rate for a vendor.

    Args:
        vendor: The Vendor object for whom to calculate the rate.

    Returns:
        The fulfillment rate as a float (0.0 to 1.0).
    """

    total_orders = PurchaseOrder.objects.filter(vendor_no=vendor)
    successful_orders = total_orders.filter(status='completed')
    # print(" kkhn berobi re",len(successful_orders) / len(total_orders))
    return len(successful_orders) / len(total_orders) if total_orders else 0.0

@receiver(post_save, sender=PurchaseOrder)
def update_historical_performance_on_completion(sender, instance, created, **kwargs):
    if created:
        
        vendor = instance.vendor_no
        
     

        on_time_delivery_rate = calculate_on_time_delivery_rate(vendor)
        quality_rating_avg = calculate_quality_rating_avg(vendor)
        average_response_time = calculate_average_response_time(vendor)
        fulfillment_rate = calculate_fulfillment_rate(vendor)
        # print(on_time_delivery_rate,quality_rating_avg,average_response_time,fulfillment_rate)

        performance, created = HistoricalPerformance.objects.get_or_create(vendor=vendor)
        # print("eto obdhi kaj korle nach")
        performance.date = datetime.now()
        performance.on_time_delivery_rate = on_time_delivery_rate
        performance.quality_rating_avg = quality_rating_avg
        performance.average_response_time = average_response_time
        performance.fulfillment_rate = fulfillment_rate
        performance.save()