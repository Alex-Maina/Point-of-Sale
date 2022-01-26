import csv

class Product:
    all = []
    #Instance to create a customer
    def __init__(self, id: str, name: str, quantity:int, price:float):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        
        #add to list everytime an instance is created
        Product.all.append(self)
    #represent the objects in a readerble manner    
    def __repr__(self):
        return f"Product('{self.id}','{self.name}','{self.quantity}','{self.price}')"
    
#product creation 
def createProduct():
    product_id = input("Assign product ID: ")
    #checks if another similar ID already exists
    checker=[]
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            checker.append(row[0])
            
    exist = checker.count(product_id)
    if exist == 1:
        print ("The ID already exists. Enter a valid one")
        exit
        createProduct ()
    else:
        #after validating the ID the user can enter the other details
        name = input("Enter the product name: ").title()
        quantity = int(input("Enter the quantity of the product: "))
        price = float(input("Enter the price: "))
        product = Product(product_id, name, quantity, price)
    
    #append the instance to a csv file
    with open("products.csv","a", newline='') as product_file:
        writer = csv.writer(product_file)
        for instance in Product.all:
            writer.writerow([instance.id, instance.name, instance.quantity, instance.price])


#overwrites the CSV file
def updateFile(updatedList):
    with open("products.csv","w", newline='') as product_file:
        writer = csv.writer(product_file)
        writer.writerows(updatedList)
    


#product deletion 
def deleteProduct():
    
    print ()
    print("Delete product")
    delete_id = input("Enter the product ID: ")
    #checks if the entered ID exists
    checker=[]
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            checker.append(row[0])
    exist = checker.count(delete_id)
    if exist == 0:
        print ("The ID entered does not exist. Enter a valid one")
        deleteProduct ()
    else:
        #writes every row except the row with the entered ID
        updatedList=[]
        with open('products.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0]!= delete_id:
                    updatedList.append(row)
        updateFile(updatedList)
        
        print("Product deleted successfully")
       
    
    

#update product 
def updateProduct():
    print ()
    print("Update product")
    update_id = input("Enter the product ID: ")
    #checks if the entered ID exists
    checker=[]
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            checker.append(row[0])
    exist = checker.count(update_id)
    if exist == 0:
        print ("The ID entered does not exist. Enter a valid one")
        updateProduct ()
    else:
        #writes every row to a list except the row with the entered ID
        edit = []
        updatedList=[]
        with open('products.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0]==update_id:
                    edit.append(row)
                elif row[0]!= update_id:
                    updatedList.append(row)
        updateFile(updatedList)
        
        #updating the list of
        print ("Entry to be updated is: ")
        print (edit)
        name = input("Update the name of the product: ").title()
        edit[0][1] = name
        quantity = input("Update the quantity of the product: ")
        edit[0][2] = quantity
        price = input("Update the price of the product: ")
        edit [0][3] = price
        print (edit)
        with open("products.csv","a", newline='') as products_file:
            writer = csv.writer(products_file)
            for instance in edit:
                writer.writerow([update_id, name, quantity, price])
    
def list_products():
    products = []
    with open('products.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                products.append(row)
    for i in range(len(products)) : 
        for j in range(len(products[i])) : 
            print(products[i][j], end=" ")
        print()    

def search_product ():
    print("Search product")
    searchName = str(input("Enter the name of the product: ")).title()
    #checks if the entered name exists
    searchList=[]
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1]==searchName:
                searchList.append(row)
    
        print(searchList)    
    
       
        






