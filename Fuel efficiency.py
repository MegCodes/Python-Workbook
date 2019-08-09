#Draft
mpg = int(input("Please enter fuel efficiency in miles per gallon: "))
l_100 = 235.215 
result = str(mpg * l_100) 
print("It equals {} in liters per hundreed kilometers.".format(result))

#v2
def f_efficiency(mpg):
    l_100 = 235.215 
    result = mpg * l_100
    print(result)
    
f_efficiency(4)    

#v3
def f_efficiency():
    mpg = int(input("Please enter fuel efficiency in miles per gallon: "))
    result = mpg * 235.215
    print(result)
    
f_efficiency()    

#v4
def f_eff():
    print(int(input("Please enter fuel efficiency in miles per gallon: ")) * 235.215)
    
f_eff() 

#v5
def f_eff(mpg):
    print(mpg * 235.215)
    
f_eff(3)    
f_eff(2)
f_eff(7)