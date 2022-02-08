# **CUSTOMER-PRODUCT POS SYSTEM**

## **Overview**

This is a customer-product PoS system which is based on
customers, products, and purchases made
by customers. The main purpose of this project is to **implement a Python program that starts with a menu**, **get user choices**, and
**process the given choices**. 

This program will assist in managing customer and product data in the
system, as well as enable customers make purchases of the products in stock. Therefore, the program will allow the user to create a new customer, update the customer information, search for a customer, and delete a customer from the system. Additionally, the user will also be able to add new products, update the existing products, search the products, and also delete products. Finally, with the customer IDs and product IDs in the system, purchases can be made.

**Language Used**: Python

**How to execute**: Run [main.py](https://github.com/Alex-Maina/Point-of-Sale/blob/master/main.py) file
   

# Functionalities
The Program starts with a main menu which prompts the user to 
 1. Enter the customer section
 2. Enter the pr section
 3. Make a purchase
 
## 1. Customer Operations
The customer operations are included in the customer section. They include adding a new customer (*each with a unique ID*), updating a customer's data except the customer ID, listing all the customers, searching a customer, and deleting a customer.

The customer data is saved in a CSV file

## 2.Products operations
The products operations are included in the products section. They include adding a new product (*each with a unique ID*), updating a product's data data except the customer ID, listing all the products, searching a for product by typing the name of the product, and deleting a product.

The products data is also saved in a CSV file.

## 3. Purchasing Operations
To make a purchase, first, the user ought to provide a valid customer ID. If the customer does not eit on the sytem, the user will be prompted to add a new customer. 

Additionally, a valid Product ID will be required to proceed with the purchase. If the order placed on an item exceeds the quantity in-stock, the customer is promted to either lower the order or purchase another product.

A customer can buy multiple items at a go and the total amount will be calculated upon checking out. A receipt is genereated upon successful purchase and the inventory is updated accodingly.
