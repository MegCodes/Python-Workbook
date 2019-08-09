#v1 - draft
def even_or_odd():
    num = int(input('Enter a number you want to check: '))
    if num % 2 == 0:
        print ('{} is even.'.format(num))
    else:
        print('{} is odd.'.format(num))

even_or_odd()

#v2 - shorter
def even_or_odd():
    num = int(input('Enter a number you want to check: '))
    print ('{} is even.'.format(num)) if num % 2 == 0 else print('{} is odd.'.format(num))

even_or_odd()

#v3 - stable
def even_or_odd():
    num = input('Enter a number you want to check (q to quit): ')
    while True:
        if num == 'q':
            break
        elif num == '' or  num == ' ':
            print('Please enter a number or q to quit')
        elif int(num) % 2 == 0:
            print ('{} is even.'.format(num))
        elif int(num) % 2 != 0:
            print('{} is odd.'.format(num))


        num = input('Enter a number you want to check(q to quit): ')

even_or_odd()