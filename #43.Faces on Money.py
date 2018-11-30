#1
note = int(input('Please enter a note amount: '))

if note == 1:
    print('George Washington')
elif note == 2:
    print('Thomas Jefferson')
elif note > 2 and note < 5:
    print('Such a note does not exist.')
elif note == 5:
    print('Abraham Lincoln')
elif note > 5 and note < 10:
    print('Such a note does not exist.')
elif note == 10:
    print('Alexander Hamilton')
elif note > 10 and note < 20:
    print('Such a note does not exist.')
elif note == 20:
    print('Andrew Jackson')
elif note > 20 and note < 50:
    print('Such a note does not exist.')
elif note == 50:
    print('Ulysses S. Grant')
elif note > 50 and note < 100:
    print('Such a note does not exist.')
elif note == 100:
    print('Benjamin Franklin')



#2
def face_on_money():
    note = int(input('Please enter a note amount (0 to quit): '))
    while True:
        if note == 0:
            break
        elif note == 1:
            print('George Washington')
        elif note == 2:
            print('Thomas Jefferson')
        elif note > 2 and note < 5:
            print('Such a note does not exist.')
        elif note == 5:
            print('Abraham Lincoln')
        elif note > 5 and note < 10:
            print('Such a note does not exist.')
        elif note == 10:
            print('Alexander Hamilton')
        elif note > 10 and note < 20:
            print('Such a note does not exist.')
        elif note == 20:
            print('Andrew Jackson')
        elif note > 20 and note < 50:
            print('Such a note does not exist.')
        elif note == 50:
            print('Ulysses S. Grant')
        elif note > 50 and note < 100:
            print('Such a note does not exist.')
        elif note == 100:
            print('Benjamin Franklin')
        else:
            print('Such a note does not exist.')

        note = int(input('Please enter a note amount (0 to quit): '))

face_on_money()


#3
def face_on_money(note):
    if note == 1:
        print('George Washington')
    elif note == 2:
        print('Thomas Jefferson')
    elif note > 2 and note < 5:
        print('Such a note does not exist.')
    elif note == 5:
        print('Abraham Lincoln')
    elif note > 5 and note < 10:
        print('Such a note does not exist.')
    elif note == 10:
        print('Alexander Hamilton')
    elif note > 10 and note < 20:
        print('Such a note does not exist.')
    elif note == 20:
        print('Andrew Jackson')
    elif note > 20 and note < 50:
        print('Such a note does not exist.')
    elif note == 50:
        print('Ulysses S. Grant')
    elif note > 50 and note < 100:
        print('Such a note does not exist.')
    elif note == 100:
        print('Benjamin Franklin')
    else:
        print('Such a note does not exist.')


face_on_money(1)
face_on_money(2)
face_on_money(4)
face_on_money(5)
face_on_money(10)
face_on_money(20)
face_on_money(25)
face_on_money(50)
face_on_money(55)
face_on_money(100)    