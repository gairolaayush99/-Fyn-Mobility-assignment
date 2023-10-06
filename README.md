# Mobilty
Mobility is a Django-based application that provides calculate the price according to pricing model and input wait time and distance for automobiles.

## Prerequisites:

Python 3.x
Django (latest version)
Getting Started
Clone the repository:



## Install Dependencies:

pip install -r requirements.txt


## Run Migrations:
```
python manage.py makemigrations
python manage.py migrate
Start the Development Server:
```
```
python manage.py runserver
Your project will be accessible at http://localhost:8000/.
```
## API Endpoints:

### 1. Home Endpoint:
```
URL: /
Method: GET
Description: Test endpoint to ensure the Django application is running.
Response:
Status Code: 200 OK
Content: "Hello, Django!"
```

### 2. Manage Pricing Configuration:
```
URL: /manage_pricing_config/
Methods: GET, POST
Description: View and manage pricing configurations.
Request:
Method: POST
Parameters: Pricing configuration data (form fields)
Response:
Status Code: 200 OK (on successful POST)
Status Code: 400 Bad Request (on invalid form data)
Example:
POST Request Body:
json
{
  "tier": "Standard",
  "day": "Monday",
  "DBP": 10,
  "DAP": 0.5,
  "TMF": 2,
  "WC": 5
}
Response:
json
{
  "message": "Pricing configuration created successfully."
}
```

### 3. Pricing Calculator Endpoint:
```
URL: /calculate_price/
Method: POST
Description: Calculate pricing based on provided input data.
Request:
Method: POST
Parameters:
tier: Pricing tier (Standard, Premium, Luxury)
day: Day of the week (Monday, Tuesday, ..., Sunday)
Tn: Time (in some unit)
Dn: Distance (in some unit)
Response:
Status Code: 200 OK (on successful calculation)
Status Code: 400 Bad Request (on invalid input or no active pricing configuration found)
Example:
POST Request Body:
json
Copy code
{
  "tier": "Standard",
  "day": "Monday",
  "Tn": 30,
  "Dn": 10
}
Response:
json
Copy code
{
  "Price": 25.0
}
Error Response (No active pricing configuration found):
json
Copy code
{
  "error": "No active pricing configuration found for the specified tier and day."
}
```
