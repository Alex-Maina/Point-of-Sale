customers = [["2a","Winnie","Ndura Str Ruaka"],["3a","Maina","Wood Av Roslyn"]]



textfile = open("customers.txt", "w")
for lists in customers:
    textfile.write((' - '.join(lists)) + "\n")
textfile.close()
file = open("customers.txt", "r")
for lines in file:
    print (lines + "\n")