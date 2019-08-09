#v1
from math import sqrt

def fall():
    height = float(input("Enter height from which the object is dropped in meters: "))
    v_1 = 0 
    gravitation = 9.8
    v_2 = round(sqrt(v_1 **2 + 2 * (gravitation * height)),2)
    print('Free fall is {}.'.format(v_2))
    
fall() 

#v2 - optimized
from math import sqrt

def fall():
    height = float(input("Enter height from which the object is dropped in meters: "))
    gravitation = 9.8
    v_2 = round(sqrt(2 * (gravitation * height)),2)
    print('Free fall is {}.'.format(v_2))
    
fall()  