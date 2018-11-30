#1
def holidayDate(month, date):
    if month == 1 and date == 1:
        print("New Year's Day")
    elif month == 7 and date == 1:
        print("Canada day")
    elif month == 12 and date == 25:
        print("Christmas day")
    else:
        print("There is no a fixed-date holiday on this day.")

holidayDate(12,25)
holidayDate(1,1)
holidayDate(7,1)
holidayDate(4,1)

#2
def holidayDate():
    month = int(input('Enter month with an integer, please: '))
    date = int(input('Enter date with the same way, please: '))

    if month == 1 and date == 1:
        print("New Year's Day")
    elif month == 7 and date == 1:
        print("Canada day")
    elif month == 12 and date == 25:
        print("Christmas day")
    else:
        print("There is no a fixed-date holiday on this day.")

holidayDate()


#3
def holidayDate():
    month = int(input('Enter month with an integer, please: '))
    date = int(input('Enter date with the same way, please: '))

    while True:
        if month == 1 and date == 1:
            print("New Year's Day")
        elif month == 7 and date == 1:
            print("Canada day")
        elif month == 12 and date == 25:
            print("Christmas day")
        else:
            print("There is no a fixed-date holiday on this day.")

        month = int(input('Enter month with an integer, please: '))
        date = int(input('Enter date with the same way, please: '))

holidayDate()