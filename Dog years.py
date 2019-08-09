#v1 (raw)
def dog_years():
    years = int(input('Enter number of dog years: '))
    d_years = 0
    if years < 0:
        print('This is not a valid number.')
    elif years <= 2:
        d_years = 10.5 * years
    elif years > 2:
        d_years = (years - 2) * 4 + 21


    print('Your dog is actually {} years old.'.format(int(d_years)))


dog_years()

#v2
def dog_years():
    years = int(input('Enter number of dog years: '))
    d_years = int(years * 10.5 if years <= 2 else(years - 2) * 4 + 21)

    print(d_years)

dog_years()