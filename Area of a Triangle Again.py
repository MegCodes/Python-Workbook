#v1
s3 = None
while s3 is None:
    s1 = float(input("Enter length of A: "))
    s2 = float(input("Enter length of B: "))
    s3 = float(input("Enter length of C: "))

from math import sqrt
def area():
    s = (s1 + s2 + s3) / 2
    a = s * (s - s1) * (s - s2) * (s - s3)
    a = sqrt(a)
    print('Area: {}.'.format(a))
    
area()

#v2
from math import sqrt

def area():
    s3 = None
    while s3 is None:
        s1 = float(input("Enter length of A: "))
        s2 = float(input("Enter length of B: "))
        s3 = float(input("Enter length of C: "))

    s = (s1 + s2 + s3) / 2
    a = s * (s - s1) * (s - s2) * (s - s3)
    a = sqrt(a)
    print('Area: {}.'.format(a))
    
area()