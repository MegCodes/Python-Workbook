#1
def taxi_fare(d):
    fare = 4.00
    tarif = d // 140
    total = round((fare + tarif * 0.25),2)
    print(f'The travelling price is ${total}')


#2 taxi.py
def taxi_fare(d):
    fare = 4.00
    tarif = d // 140
    total = round((fare + tarif * 0.25),2)
    print(f'The travelling price is ${total}')


#taxi_display.py
from taxi import taxi_fare

d = float(input('Enter distance in kilometers: ')) * 1000

taxi_fare(d)