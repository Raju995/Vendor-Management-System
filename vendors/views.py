from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor_details
from .serializer import VendorSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HistoricalPerformance
from .serializer import HistoricalPerformanceSerializer
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes




# Vendor API Endpoints
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated]) 

def vendor_list(request):
  """
  List all vendors or create a new vendor.
  """
  if request.method == 'GET':
    vendors = Vendor_details.objects.all()
    serializer = VendorSerializer(vendors, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message":"id created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail(request, pk):
  """
  Retrieve, update or delete a vendor.
  """
  vendor = get_object_or_404(Vendor_details, pk=pk)
  if request.method == 'GET':
    serializer = VendorSerializer(vendor)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = VendorSerializer(vendor, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    vendor.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['GET'])
def get_historical_performance(request, vendor_id):
    """
    Retrieve historical performance data for a specific vendor.
    """
    try:
        vendor = Vendor_details.objects.get(pk=vendor_id)
        # print("hi ven",vendor)
    except Vendor_details.DoesNotExist:
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

    performances = HistoricalPerformance.objects.filter(vendor=vendor)
    # print(performances)
    serializer = HistoricalPerformanceSerializer(performances, many=True)
    return Response(serializer.data)
