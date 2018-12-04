print("Celcius - Fahrenheit")

for degree in range(0,101,10):
    print("\t" + str(degree) + '\t\t'  + str((degree * 9//5) + 32))