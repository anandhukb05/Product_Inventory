# Product_Inventory

# Functionality

Product Inventory API using Django REST Framework.
 
Product model with:
    name (CharField, max_length=100)
    price (DecimalField)
    stock (IntegerField)
 
API endpoints to:
    List all products
    Add a new product
    Update a product
    Delete a product
 
validation to ensure the product price is not negative.
 

Run code with command

python manage.py runserver

url : http://127.0.0.1:8000/products/


 