#Vers.1
def deposit():
    less  = 0.10
    more = 0.25
    to_one = int(input("Enter the number of containers holding 1 liter or less: "))
    more_one= int(input("Enter the number of containers holding more than 1 liter: "))
    refund = round((less * to_one) + (more * more_one),2)
    print("/nYour refund is {}$.".format(refund))
    
deposit()  

#Vers.2
def deposit():
    less  = 0.10
    more = 0.25
    to_one = int(input("Enter the number of containers holding 1 liter or less: "))
    more_one= int(input("Enter the number of containers holding more than 1 liter: "))
    refund = round((less * to_one) + (more * more_one),2)
    print(f"\nYour refund is {refund}$.")
    
deposit()  

#Vers.3 (better)
def deposit():
    less  = 0.10
    more = 0.25
    to_one = int(input("Enter the number of containers holding 1 liter or less: "))
    more_one= int(input("Enter the number of containers holding more than 1 liter: "))
    refund = round((less * to_one) + (more * more_one),2)
    print("\nYour refund is $%.2f." % refund)
    
deposit()  

#Vers.4
def deposit(to_one, more_one):
    less  = 0.10
    more = 0.25
    refund = round((less * to_one) + (more * more_one),2)
    print("\nYour refund is $%.2f." % refund)
    
deposit(4,3)  

#Vers.5
def deposit(to_one, more_one):
    less  = 0.10
    more = 0.25
    return round((less * to_one) + (more * more_one),2)
    
print(deposit(2,3))  
print(deposit(4,8))