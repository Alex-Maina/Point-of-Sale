

customers = [["2a","Winnie","Ndura Str, Ruaka"],["3a","Maina","Wood Av, Roslyn"]]



def add_customer ():
    new_customer = []
    print ()
    customer_ID = input("Assign customer ID: ")
    customer_name = input("Enter the customer name: ")
    customer_address = input("Enter the customer address: ")
    new_customer.append(customer_ID)
    new_customer.append (customer_name)
    new_customer.append (customer_address)
    print ()
    print ("Customer added successfully")
    print ()
    
    customers.append(new_customer)
   
#add_customer()

#A funtion to list all the customers (from the list)
def list_customers ():
    for i in range(len(customers)) : 
        for j in range(len(customers[i])) : 
            print(customers[i][j], end=" ")
        print()    
#list_customers ()

def update_customer ():
    #function to notify user of the update
    def update_notice ():
        print ()
        print ("Updated successfully")
        print ("Name: "+customers[index][1] +"     Address: "+customers[index][2])
        print ()
    
    #initializing index
    index = 0
    print ()
    print("Update customer")
    update_menu = input("Enter the customer ID: ")
    
    try:
        #finds the index of the list that contains the entered customer ID
        index = [i for i, lst in enumerate(customers) if update_menu in lst][0]
        
        #notify the user of the entry that has been found    
        print ()
        print ("Entry found:")
        print ("Name: "+customers[index][1] +"     Address: "+customers[index][2])
        
        
        #Sub menu - Allows user to choose what to update
        edit_choice = input("""
                        
                    1: Update Customer Name
                    2: Update Customer Address
                    3: Update Both
                    0: Back

                    Please enter your choice: """)
            
        if edit_choice == "1":
            name_update = input("Enter new name: ")
            customers [index][1]= name_update
            update_notice ()
        elif edit_choice == "2":
            address_update = input("Enter new address: ")
            customers [index][2]= address_update
            update_notice ()
        elif edit_choice == "3":
            name_update = input("Enter new name: ")
            customers [index][1]= name_update
            address_update = input("Enter new address: ")
            customers [index][2]= address_update
            update_notice ()
        elif edit_choice == "0":
            print ()
            
    #Exception handler incase the customer ID provided is not found
    except Exception as e:
        print ()
        print ("Customer ID not found. Please enter an existing customer ID")
        update_customer ()
    
    
    
#Deletion function
def delete_customer ():
    index = 0
    print ()
    print("Delete customer")
    delete_menu = input("Enter the customer ID: ")
        
    try:
        #finds the index of the list that contains the entered customer ID
        index = [i for i, lst in enumerate(customers) if delete_menu in lst][0]
        
        #notify the user of the entry that has been found    
        print ()
        print ("Entry found:")
        print ("Name: "+customers[index][1] +"     Address: "+customers[index][2])
        print ()
        customers.pop (index)
        print ("Deleted successfully")
        
    #Exception handler incase the customer ID provided is not found
    except Exception as e:
        print ()
        print ("Customer ID not found. Please enter an existing customer ID")
        index=0
        delete_customer ()
    
    
    








