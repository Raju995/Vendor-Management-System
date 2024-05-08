from django.urls import path
from .views import vendor_list, vendor_detail,get_historical_performance
from rest_framework.authtoken import views 
app_name = 'vendors'  # Define a unique app name

urlpatterns = [
  path('vendors/', vendor_list, name='vendor_list'),
  path('vendors/<int:pk>/', vendor_detail, name='vendor-detail'),
  path('vendors/<int:vendor_id>/performance/',get_historical_performance, name='vendor-historical-performance'),
  path('api-token-auth', views.obtain_auth_token, name='api-token-auth'),

]
