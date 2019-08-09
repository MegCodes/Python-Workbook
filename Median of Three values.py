#Vers.1
def med(x,y,z):
    result = x + y + z - min(x,y,z) - max(x,y,z)
    print("The median of {}, {}, {} is {}.".format(x,y,z,result))
    
med(2,5,4)
med(1,2,8)

#Vers.2
def med():
    x = float(input("Enter a number: "))
    y = float(input("Enter a second one: "))
    z = float(input("Enter the last: "))
    return x + y + z - min(x,y,z) - max(x,y,z)
    
print("The median here is ",str((med()) + '.')

#Vers.3
def med(a,b,c):
    if  a < b and  b < c:
        return b
    elif b < a and a < c:
        return a
    else:
        return c
        
print("There median is {}.".format(str(med(4,3,6))))  