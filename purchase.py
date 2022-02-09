import csv
from customer import *

print ()
print("Make a purchase")
foundCustomer = []
foundProduct = [] 
purchases=[]

#Checks whether the customer ID exists
def checkID ():
        print ()
        global customerID 
        customerID = input("Enter the customer ID to make a purchase: \n")
        #checks if the entered ID exists
        checker=[]
        with open('customer.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                checker.append(row[0])
        exist = checker.count(customerID)
        if exist == 0:
            print ("The ID entered does not exist.")
            selection = input("""
                              1. Re-enter a valid ID
                              2. Add a new customer
                              
                              Enter your choice: 
                              """)
            if selection == "1":
                checkID ()
            elif selection == "2":
                create()
                checkID () 

#Requests for the customer ID to makke a purchase
def customer():    
    checkID ()
    
    #writes the row to a list
    with open('customer.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]==customerID:
                foundCustomer.append(row)
        
        print ("Customer found: "+foundCustomer[0][1])
        

#Checks whether the product ID exists
def checkProductID ():
        print ()
        global productID 
        productID = input("Enter the product ID to make a purchase: \n")
        print ()
        #checks if the entered ID exists
        checker=[]
        with open('products.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                checker.append(row[0])
        exist = checker.count(productID)
        if exist == 0:
            print ("The ID entered does not exist. Enter a valid ID")
            checkProductID () 

#makes a sale
def sell ():    
    checkProductID ()
    
    #writes the row to a list
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]==productID:
                foundProduct.insert(0,row)
        prod = foundProduct[0][1]
        stock = int(foundProduct[0][2])
        price = float(foundProduct[0][3])
        print ("Product: "+prod)
        print ("Items in-stock: "+ str(stock))
        print ("Price: Ksh."+str(price))
        print ()
        
    amount = int(input("Enter the order quantity \n"))
    #checks if there's enough stock
    if amount > stock:
        print (prod +" cannot be sold.\nStock below placed order - In-stock: "+str(stock)+"\nPlace another order")
        sell ()
    else:
        #records purchase made to a list
        cost = amount * price
        
        #creates a list of purchases made
        purchases.append([productID,prod,price,amount,cost])
        print ()
        print (purchases)
        
        anotherPurchase = input("""
                                1. Purchase another item
                                2. Proceed to check out
                                
                                Enter your selection: """)
        if anotherPurchase == "1": 
            sell ()
        elif anotherPurchase == "2":
            checkout ()

#Checkout function
def checkout():
    sum = 0
    for purchase in purchases:
        sum += purchase[4]
    print ()
    
    cashGiven = float(input("Amount of cash given \n"))
    if cashGiven<sum:
        print ("Sorry, Insufficient funds. \nTotal amount is Ksh."+str(sum))
        choice = input("""
                       1. Enter another amount
                       0. Exit
                       
                       Enter your choice: """)
        if choice == "1":
            checkout ()
        else:
            print ("Exiting...Going back to the main menu.")
    else:
        balance = cashGiven - sum 
        print ()
        print ("Purchase Receipt:")
        print ("-----------------")
        print ("Customer:  "+ foundCustomer[0][1])
        for purchase in purchases:
            print ("Product:   "+purchase[1])
            print ("           Ksh."+str(purchase[2]))
            print ("Quantity:  *"+str(purchase[3]))
            print ("           ksh."+str(purchase[4]))
        print ()
        print ("Total:     "+str(sum))
        print ()
        print ("Cash:      ksh."+str(cashGiven))
        print ("Balance:   ksh."+str(balance))
        print ()
        print ("Purchase Complete")
        
        updateInventory()

#Updates inventory upon successful purchase
def updateInventory ():
    for purchase in purchases:
        updateID = purchase[0]
        amount = int(purchase[3])
        
        edit = []
        updatedList=[]
        with open('products.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0]==updateID:
                    edit.append(row)
                elif row[0]!= updateID:
                    updatedList.append(row)
        with open("products.csv","w", newline='') as product_file:
            writer = csv.writer(product_file)
            writer.writerows(updatedList)
        
        #updating the list 
        name = edit[0][1]
        qty = int(edit[0][2])
        edit [0][2] = qty - amount
        qnty = edit [0][2]
        price = edit [0][3] 
     
        with open("products.csv","a", newline='') as products_file:
            writer = csv.writer(products_file)
            for instance in edit:
                writer.writerow([updateID, name, qnty, price])
    print ()
    print ()          
    print("Inventory Updated")



def purchase ():
    customer()
    sell ()
