#draft
waterheat = 4.186
elect_price = 8.9
j_khw = 2.777 * 10 ** 7

def heat_capacity():
    volume = float(input("Enter water amount in milliliters: "))
    d_temp = float(input("Enter temperature increase (degrees Celsius): "))
    q = volume * d_temp * waterheat
    kwh = q * j_khw
    cost = round(kwh * elect_price)
    print('This amount of energy will cost {} cents.'.format(cost))
    
heat_capacity()