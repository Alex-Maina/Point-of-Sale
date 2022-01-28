import csv

class Customer:
    all = []
    #Instance to create a customer
    def __init__(self, id: str, name: str, address:str):
        self.name = name
        self.address = address
        self.id = id
        #add to list everytime an instance is created
        Customer.all.append(self)
    #represent the objects in a readerble manner    
    def __repr__(self):
        return f"Customer('{self.id}','{self.name}','{self.address}')"
    
#customer creation 
def create():
    def checkID ():
        global customer_id
        customer_id = input("Assign customer ID: ")
        #checks if another similar ID already exists
        checker=[]
        with open('customer.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                checker.append(row[0])
        exist = checker.count(customer_id)
        if exist != 0:
            print ("The ID already exists. Enter a valid one")
            checkID ()
    checkID ()
    
    #after validating the ID the user can enter the other details
    name = input("Enter the customer name: ")
    address = input("Enter the customer address: ")
    customer = Customer(customer_id,name,address)
    
    #append the instance to a csv file
    with open("customer.csv","a", newline='') as customer_file:
        writer = csv.writer(customer_file)
        for instance in Customer.all:
            writer.writerow([instance.id, instance.name, instance.address])


#overwrites the CSV file
def updateFile(updatedList):
    with open("customer.csv","w", newline='') as customer_file:
        writer = csv.writer(customer_file)
        writer.writerows(updatedList)
    

#customer deletion 
def delete():
    
    print ()
    print("Delete customer")
    delete_id = input("Enter the customer ID: ")
    #checks if the entered ID exists
    checker=[]
    with open('customer.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            checker.append(row[0])
    exist = checker.count(delete_id)
    if exist == 0:
        print ("The ID entered does not exist. Enter a valid one")
        delete ()
    else:
        #writes every row except the row with the entered ID
        updatedList=[]
        with open('customer.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0]!= delete_id:
                    updatedList.append(row)
        updateFile(updatedList)
        
        print("Customer deleted successfully")


#update customer 
def update():
    print ()
    print("Update customer")
    update_id = input("Enter the customer ID: ")
    #checks if the entered ID exists
    checker=[]
    with open('customer.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            checker.append(row[0])
    exist = checker.count(update_id)
    if exist == 0:
        print ("The ID entered does not exist. Enter a valid one")
        update ()
    else:
        #writes from CSV to list
        edit = []
        updatedList=[]
        with open('customer.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0]==update_id:
                    #writes the row to be updated to a list
                    edit.append(row)
                elif row[0]!= update_id:
                    #writes the other rows to another list
                    updatedList.append(row)
        updateFile(updatedList)
        
        #updating the edit list 
        print ("Entry to be updated is: ")
        print (edit)
        name = input("Update the name of the customer: ")
        edit[0][1] = name
        address = input("Update the address of the customer: ")
        edit[0][2]= address
        print (edit)
        #insert the updated list to the CSV file
        with open("customer.csv","a", newline='') as customer_file:
            writer = csv.writer(customer_file)
            for instance in edit:
                writer.writerow([update_id, name, address])
    
def list_customers ():
    customers = []
    with open('customer.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                customers.append(row)
    for i in range(len(customers)) : 
        for j in range(len(customers[i])) : 
            print(customers[i][j], end=" ")
        print()    
        