from django.urls import path
# from .views import (
#     create_purchase_order,
#     list_purchase_orders,
#     purchase_order_detail,
# )
from .views import (
    
   list_purchase_orders,
    purchase_order_detail,
    update_acknowledgment,
)

app_name = 'po'  # Define a unique app name

urlpatterns = [
    # path('', purchase_orders, name='purchase_orders'),
    path('', list_purchase_orders, name='list_purchase_orders'),  # Same path for listing with query param
    path('<int:pk>/', purchase_order_detail, name='purchase-order-detail'),
    path('<int:pk>/acknowledge/',update_acknowledgment,name='update_acknowledgment'),
]
