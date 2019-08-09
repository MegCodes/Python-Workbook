#v1 (raw and unrevised)
nums = input('Enter 4 numbers: ')
sum = 0
for num in nums:
    sum == int(num)
    sum += int(num)

print(sum)

#v2
def sum():
    nums = input('Enter 4 numbers: ')
    intsum = 0
    for num in nums:
        intsum += int(num)
    return intsum

print(sum())

#v3
def sum():
    nums = input('Enter 4 numbers (q to quit): ')
    sum = 0
    while True:
        if nums == 'q':
            break
        elif nums == '' or nums == ' ':
            print('No numbers provided.')
            nums = input('Enter 4 numbers (q to quit): ')
        elif nums:
            for num in nums:
                    sum == int(num)
                    sum += int(num)
            return sum

print(sum())