#Vers.1
def arithmetic():
    from math import log10
    a = int(input("Enter an integer: "))
    b = int(input("Enter an integer: "))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
    print(log10(a))
    print(a ** b)
    
arithmetic()

#Vers.2
def arithmetic(a,b):
    from math import log10
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
    print(log10(a))
    print(a ** b)
    
arithmetic(8,7)
arithmetic(6,7)