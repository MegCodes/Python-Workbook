def area_volume():
    r = int(input("Enter a radius: "))
    from math import pi
    area = round(pi * r ** 2,2)
    volume = round(4 / 3 * pi * r ** 3,2)
    print('Area: {}. \nVolume: {}.'.format(area, volume))
    
area_volume()