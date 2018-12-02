#1
from statistics import mean

thelist = []

while True:
    values = int(input('Please enter values (zero to quit): '))

    if values != 0:
        thelist.append(values)
    else:
        break


if thelist:
    print((thelist))
    print(mean(thelist))
else:
    print('Thanks for your time!')