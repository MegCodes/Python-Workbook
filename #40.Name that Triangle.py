#1
a_side = int(input('Enter 1st side in cm: '))
b_side = int(input('Enter 2nd side in cm: '))
c_side = int(input('Enter 3rd side in cm: '))

if a_side == b_side and b_side == c_side:
    print("It is an equilateral triangle.")
elif a_side == b_side and a_side != c_side:
    print("It is an isosceles triangle.")
else:
    print("It is a scalene triangle.")


#2
def triangle_name():
    a_side = int(input('Enter 1st side in cm: '))
    b_side = int(input('Enter 2nd side in cm: '))
    c_side = int(input('Enter 3rd side in cm: '))

    if a_side == b_side and b_side == c_side:
        print("It is an equilateral triangle.")
    elif a_side == b_side and a_side != c_side:
        print("It is an isosceles triangle.")
    else:
        print("It is a scalene triangle.")

triangle_name()


#3
def triangle_name():
    print('Press 0 to quit.')
    a_side = int(input('Enter 1st side in cm: '))
    b_side = int(input('Enter 2nd side in cm: '))
    c_side = int(input('Enter 3rd side in cm: '))
    while True:
        if a_side == 0 or b_side == 0 or c_side ==0:
            break
        elif a_side == b_side and b_side == c_side:
            print("It is an equilateral triangle.")
        elif a_side == b_side and a_side != c_side:
            print("It is an isosceles triangle.")
        else:
            print("It is a scalene triangle.")

        print('Press 0 to quit at any time')
        a_side = int(input('Enter 1st side in cm: '))
        b_side = int(input('Enter 2nd side in cm: '))
        c_side = int(input('Enter 3rd side in cm: '))

triangle_name()

#4
def triangle_name(a_side, b_side, c_side):
    if a_side == b_side and b_side == c_side:
        print("It is an equilateral triangle.")
    elif a_side == b_side and a_side != c_side:
        print("It is an isosceles triangle.")
    else:
        print("It is a scalene triangle.")


triangle_name(4,4,2)
triangle_name(5,5,5)
triangle_name(3,2,1)