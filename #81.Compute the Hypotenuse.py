#1
from math import sqrt

def hypotenuse():
    print("Enter length of triangle sides")
    a = float(input("a: "))
    b = float(input('b: '))
    c = round(sqrt(a ** 2 + b ** 2),2)
    print(f'Length of hypotenuse is {c}.')

hypotenuse()

#2 hypotenuse.py
from math import sqrt

def hypotenuse(a,b):
    c = round(sqrt(a ** 2 + b ** 2),2)
    print(f'Length of hypotenuse is {c}.')

#display.py
from hypotenuse import hypotenuse

print("Enter length of triangle sides")
side1 = float(input("a: "))
side2 = float(input('b: '))

hypotenuse(side1,side2)