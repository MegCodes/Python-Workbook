def days_in_month():
    month = input('Enter name of the month (q to quit): ').title()
    thirty_days = ['April', 'June', 'September', 'November']
    while True:
        if month == 'Q':
            break
        elif month in thirty_days:
            print(f'{month} has 30 days in it.')
        elif month == 'February':
            print(f'{month} has 28 or 29 days, depending whether it is a leap year or not.')
        else:
            print(f'{month} lasts 31 days.')
        month = input('Enter name of the month (q to quit): ').title()

days_in_month()