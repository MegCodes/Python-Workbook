data = []
val = int(input("Enter a number (press 0 to quit):"))
while val != 0:
    data.append(val)
    val = int(input("Enter a number (press 0 to quit):"))
data.sort()

print('The numbers in ascending order are:')
for number in data:
    print(number)