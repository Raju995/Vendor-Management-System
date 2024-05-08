
# Vendor Management System

This project provides a well-structured and secure Django REST API for managing vendors in a system. It leverages the power of Django REST Framework for efficient API development and utilizes token authentication to ensure secure access to your vendor data.





## Key Features
* **Vendor Management**: Create, retrieve, update, and delete vendor information.
* **Historical Performance**: Track and access historical performance data for each vendor.
* **Purchase Order Management**: Create, retrieve, update, and delete purchase orders associated with vendors.
* **Token Authentication**: Secure your API with token-based authentication for authorized access.
## Prerequisites
* Python (version 3.x recommended)
* Django
* Django REST Framework
## Installation
1. **Create a Virtual Environment**
```
python -m venv venv  # Linux/macOS
source venv/bin/activate  # Linux/macOS

# OR (For Windows)
venv\Scripts\activate.bat  # Windows
```
2. **Install Required Dependencies**
Once your virtual environment is activated, install the necessary packages using pip

```
pip install django
pip install django djangorestframework
```
3. **Clone or Download the Project Repository**

Obtain the project code from a version control system (e.g., Git) or download it directly.

## Project Setup
1. **Navigate to the Project Directory**
Use the cd command in your terminal to navigate to the directory where you downloaded the project code.

2. **Run Migrations**
```
python manage.py makemigrations  # Creates migrations
python manage.py migrate         # Applies migrations to database


```

3. **Start the Development Server**

Run the Django development server to start the API and be able to access it in your web browser. This will typically start the server on http://127.0.0.1:8000/. You can use this command:

```
python manage.py runserver

```
## API Reference

This section guides you through documenting the API endpoints within your Vendor Management System project

Clearly state that the API utilizes token-based authentication for security. Users need a valid token to access these endpoints. You can obtain a token through the Django admin panel or other authentication mechanisms 

### Prerquisites

Before interacting with these API endpoints, ensure you have a user account created within the system. User creation can be done through the Django admin panel or other configured authentication mechanisms

For create a super user please enter the following commmand

```
python manage.py createsuperuser
```



#### Authorization

Clearly state that the API utilizes token-based authentication for security. Users need a valid token to access these endpoints. You can obtain a token through the Django admin panel or other authentication mechanisms 

```http
  GET /api/api-token-auth
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | Django User|
| `password` | `string`| User password|

#### Vendor Profile Management

##### Create a Vendor
```POST
  POST /api/items/vendors/
```
Also pass token in Authorization

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name of the Vendor |
| `contact_details`      | `string` | **Required**. Contact Details of Vendor |
| `address`      | `string` | **Required**.Address of the vendor |
| `vendor_code`      | `string` | **Required**. Vendor code should be unique and not null |

#### Fetch list of Vendors

```POST
  GET /api/items/vendors/
```
Also pass token in Authorization

#### Details of Particular Vendor

```POST
  GET /api/items/vendors/<int:pk>/'

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_code`      | `string` | **Required**. Vendor_code of that particular vendor|

Also pass token in Authorization

#### Delete Details of Particular Vendor

```POST
  Delete/api/items/vendors/<int:pk>/

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `vendor_code`      | `string` | **Required**. Vendor_code of that particular vendor|



#### Update Details of Particular Vendor

```POST
  PUT/api/items/vendors/{vendor_code}/

```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name of the Vendor |
| `contact_details`      | `string` | **Required**. Contact Details of Vendor |
| `address`      | `string` | **Required**.Address of the vendor |
| `vendor_code`      | `string` | **Required**. Vendor code should be unique and not null |


Summarisation of Vendor API View:

| Endpoint | Method   | Description                       |
| :-------- | :------- | :-------------------------------- |
| /api/items/vendors/      | POST | Create a new vendor |
|/api/items/vendors/      | GET | List all vendor details |
| /api/items/vendors/{vendor_code}/     | GET | Details of a particular Vendor |
| /api/items/vendors/{vendor_code}/       | PUT | Update details of a particular vendor |
| /api/items/vendors/{vendor_code}/       |Delete | Delete details of a particular vendor |

### Purchase order Management

#### Create a purchase order

```POST
  POST api/purchase_orders/
```
Also pass token in Authorization

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| po_number     | `string` | **Primary Key** po_number should be unique and not null |
| vendor_no     | `string` | **Foreign Key** It should be referencing to vendors table |
| order_date     | `Datetime` | Datetime when order is placed |
| delivery_date   | `Datetime`|  Datetime when order is going to be delivered |
| items   | `JSON`| Items which are ordered |
| quantity   | `Integer`|Quantity of ordered items |
| status   | `String`| Current status of the purchase order (pending, completed, cancelled).|
| quality_rating   | `float`| Quality rating for the purchase order |
| issue_date   | `Datetime`| Date and time the purchase order was issued to the vendor|
| acknowledgment_date   | `Datetime`| Date and time the vendor acknowledged the purchase order |
| acknowledgment_status   | `String`| Indicates whether the vendor acknowledged the purchase order ("yes" or "no"). |


#### Fetch list of purchase purchase_orders

```POST
  GET api/purchase_orders/
```
#### Details of a particular purchase order

```POST
  GET api/purchase_orders/{po_number}/
```
#### Update details of a particular purchase order

```POST
  PUT api/purchase_orders/{po_number}/
```

#### Delete details of a particular purchase order

```POST
  DELETE api/purchase_orders/{po_number}/
```
#### Vendor acknowledge of particular Purchase order

```POST
  POST api/purchase_orders/{po_number}/acknowledge/
```

Summarisation of Purchase Order API

| Endpoint | Method    | Description                       |
| :-------- | :------- | :-------------------------------- |
|api/purchase_orders/    | GET | Fetch list of purchase orders |
| api/purchase_orders/     | POST  | Create a purchase order |
| api/purchase_orders/{po_number}/     | GET |Details of a particular purchase order |
| api/purchase_orders/{po_number}/   | PUT|  Update Details of a particular purchase order|
| api/purchase_orders/{po_number}/   | DELETE| Delete details of a particular purchase order|
| api/purchase_orders/{po_number}/acknowledge/  | POST|Vendor acknowledge of particular Purchase order|

### Historical performance of Vendor

Historical performance of vendor

```POST
  GET api/vendors/{vendor_code}/performance/
```
Details of Response of Historical Performance of a vendor

| Parameter| Type   | Description                       |
| :-------- | :------- | :-------------------------------- |
|vendor  | `String`|Vendor code of particular vendor|
| Date     | `Datetime`  | Date of the historical performance get updated |
| on_time_delivery_rate    | `Float` |Rating of on time delivery |
|quality_rating_avg | `Float`|  Average of quality rating|
|average_response_time | `Float`|  Average of response time|
|fulfillment_rate | `Float`|  Average of fulfillment_rate|



















