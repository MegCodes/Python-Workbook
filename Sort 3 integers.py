#v1
def sort_3():
    nums = input('Enter 3 numbers: ')
    nums = list(nums)
    large = int(max(nums))
    low = int(min(nums))
    middle = 0
    for num in nums:
        middle += int(num)

    middle = middle - low - large

    print('The largest value is: ', large)
    print('The lowest value is: ', low)
    print('The middle value is: ', middle)

sort_3()

#v2
def sort_3():
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    c = int(input('Enter a number: '))

    large = max(a,b,c)
    low = min(a,b,c)
    middle = (a + b + c) - low - large


    print('The largest value is: ', large)
    print('The lowest value is: ', low)
    print('The middle value is: ', middle)

sort_3()

#v3
def sort_3():
    nums = input('Enter 3 numbers(e to exit):')
    while True:
        if nums == 'e':
            break
        elif nums == '' or nums == ' ':
            print('Not valid.')
            nums = input('Enter 3 numbers(e to exit):')
        elif nums != 'e' and nums != '' and nums != ' ':
            nums = list(nums)
            large = int(max(nums))
            low = int(min(nums))
            middle = 0
            for num in nums:
                middle += int(num)

            middle = middle - low - large

            print('Maximum: ', large)
            print('Minimum: ', low)
            print('Middle: ',middle)
            nums = input('Enter 3 numbers(e to exit):')

sort_3()