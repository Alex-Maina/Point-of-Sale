import csv
import sys




checker=[]
with open('customer.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        checker.append(row[0])
    
print(checker)
exist = checker.count("123")
if exist == 1:
    print("you have to reenter")
    

    
