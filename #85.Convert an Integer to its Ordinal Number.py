#1
while True:
    i = int(input('Enter a number from 1 till 12(inclusive): '))

    def to_ordinal(num):
        if num == 1:
            print('first')
        elif num == 2:
            print('second')
        elif num == 3:
            print('third')
        elif num == 5:
            print('fifth')
        elif num == 4:
            print('fourth')
        elif num == 6:
            print('sixth')
        elif num == 7:
            print('seventh')
        elif num == 8:
            print('eighth')
        elif num == 9:
            print('ninth')
        elif num == 10:
            print('tenth')
        elif num == 11:
            print('eleventh')
        elif num == 12:
            print('twelveth')

    if i > 12 or i == 0:
        print("It's not a correct value, please, try again.")
    else:
        to_ordinal(i)

#2
while True:
    try:
        i = int(input('Enter a number from 1 till 12(inclusive): '))

    except:
        print("It's not a correct value, please, try again.")

    def to_ordinal(num):
        if num == 1:
            print('first')
        elif num == 2:
            print('second')
        elif num == 3:
            print('third')
        elif num == 5:
            print('fifth')
        elif num == 4:
            print('fourth')
        elif num == 6:
            print('sixth')
        elif num == 7:
            print('seventh')
        elif num == 8:
            print('eighth')
        elif num == 9:
            print('ninth')
        elif num == 10:
            print('tenth')
        elif num == 11:
            print('eleventh')
        elif num == 12:
            print('twelveth')

    if i > 12 or i == 0:
        print("It's not a correct value, please, try again.")
    else:
        to_ordinal(i)