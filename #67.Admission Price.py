total = 0

while True:
    guest = input('Please enter your age: ')

    if str(guest) == '' or str(guest) == ' ':
        print('The admission price is ${:.2f}. Enjoy your stay!'.format(total))
        total = 0
    elif int(guest) <= 2:
        total += 0
    elif int(guest) >= 3 and int(guest) <= 12:
        total += 14.00
    elif int(guest) >= 65:
        total += 18.00
    else:
        total += 23.00