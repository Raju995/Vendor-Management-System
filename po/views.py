from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PurchaseOrder
from .serializer import PurchaseOrderSerializer, PurchaseOrderListSerializer,Acknowledge
from vendors.models import Vendor_details  # Assuming vendor_app exists

# Purchase Order API Endpoints

# @api_view(['POST'])

 
@api_view(['GET','POST'])
def list_purchase_orders(request):
    """
    List all purchase orders with optional vendor filtering.
    Include complete vendor details in the response.
    """
    if request.method == 'GET':
        vendor_id = request.query_params.get('vendor_no')
        print(vendor_id)
        if vendor_id:
            purchase_orders = PurchaseOrder.objects.filter(vendor=vendor_id)
        else:
            purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
         serializer = PurchaseOrderSerializer(data=request.data)
         print(request.data)
         if serializer.is_valid():
            vendor_id = request.data.get('vendor_no')
            print("ven id",vendor_id)
            if not vendor_id:
                return Response({'error': 'Vendor ID is required'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                print("hi it is working")
                vendor = Vendor_details.objects.get(pk=vendor_id)
                print("hi vendor",vendor)
            except Vendor_details.DoesNotExist:
                return Response({'error': 'Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       

# @api_view(['POST', 'GET'])
# def purchase_orders(request):
#     """Create a new purchase order or list all purchase orders."""
#     if request.method == 'POST':
#         # Create a new purchase order
#         vendor_id = request.data.get('Vendor_details')
#         if not vendor_id:
#             return Response({'error': 'Vendor ID is required'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             vendor = Vendor_details.objects.get(pk=vendor_id)
#         except Vendor_details.DoesNotExist:
#             return Response({'error': 'Vendor does not exist'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = PurchaseOrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(vendor=vendor)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         # List all purchase orders with optional vendor filtering
#         vendor_id = request.query_params.get('Vendor_details')
#         if vendor_id:
#             purchase_orders = PurchaseOrder.objects.filter(vendor=vendor_id)
#         else:
#             purchase_orders = PurchaseOrder.objects.all()
#         serializer = PurchaseOrderListSerializer(purchase_orders, many=True)
#         return Response(serializer.data)

    # If request method is neither POST nor GET
    # return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def purchase_order_detail(request, pk):
  """Retrieve, update or delete a purchase order."""
  purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
  if request.method == 'GET':
    serializer = PurchaseOrderSerializer(purchase_order)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    purchase_order.delete

@api_view(['POST'])
def update_acknowledgment(request, pk):
    """
    Update acknowledgment status and date for a purchase order.
    """
    try:
        purchase_order = PurchaseOrder.objects.get(pk=pk)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.data.get('acknowledgment_status') not in ['yes', 'no','Yes','No']:
        return Response({'error': 'Invalid acknowledgment status'}, status=status.HTTP_400_BAD_REQUEST)

    purchase_order.acknowledgment_status = request.data.get('acknowledgment_status')
    print(purchase_order.acknowledgment_status)
    if purchase_order.acknowledgment_status=="Yes" or purchase_order.acknowledgment_status=="yes":
      purchase_order.acknowledgment_date = datetime.now()  # Set acknowledgment timestamp on update
      purchase_order.save()

    serializer = Acknowledge(purchase_order)
    return Response(serializer.data)
