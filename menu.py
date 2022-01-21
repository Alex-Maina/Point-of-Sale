from customer import *
from products import *
from purchase import *


def menu ():
    #Initialising choice_main_menu
    choice_main_menu = 0
    while choice_main_menu != "0":
        print ()
        print ("CLI Driven E-commerce System")
        choice_main_menu = input("""
                        
                      1: Enter Customer Section
                      2: Enter Products Section
                      3: Make a Purchase
                      0: Exit

                      Please enter your choice: """)

        #Sub menu - CRUD Operations on customers
        if choice_main_menu == "1":
            print ()
            customer_sub_menu = input("""
                        
                        1: Add a new customer
                        2: Update customer data
                        3: Delete a Customer
                        4: List all customers
                        0: Back

                      Please enter your choice: """)

            if customer_sub_menu == "1":
                add_customer ()
            elif customer_sub_menu == "2":
                update_customer ()
            elif customer_sub_menu == "3":
                delete_customer ()
            elif customer_sub_menu == "4":
                list_customers ()
            elif customer_sub_menu == "0":
                print ()
            else:
                print("Invalid choice. Please try again")
    
    
        #Sub menu - CRUD Operations on products
        elif choice_main_menu == "2":
            print ()
            product_sub_menu = input("""
                        
                        1: Add a new product
                        2: Update product data
                        3: Delete a product
                        4: List all products
                        5: Search a product
                        0: Back

                      Please enter your choice: """)

            if product_sub_menu == "1":
                add_product ()
            elif product_sub_menu == "2":
                update_product ()
            elif product_sub_menu == "3":
                delete_product ()
            elif product_sub_menu == "4":
                list_products ()
            elif product_sub_menu == "5":
                search_product ()
            elif product_sub_menu == "0":
                print ()
            else:
                print("Invalid choice. Please try again") 
        

        #Sub menu - Making a purchase
        elif choice_main_menu == "3":
            purchase ()

        elif choice_main_menu == "0":
            print ("Exiting")
            print ("Thanks for using this program")
        
        else:
            print("Invalid choice. Please try again")
        


def write_file():
    textfile = open("customers.txt", "w")
    textfile = open("customers.txt", "w")
    for lists in customers:
        textfile.write((' - '.join(lists)) + "\n")
    textfile.close()
    file = open("customers.txt", "r")
    for lines in file:
        print (lines + "\n")

    