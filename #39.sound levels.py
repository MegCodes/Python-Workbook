#Version 1
noise = int(input('Enter the sound level in decibels: '))

if noise < 40:
    print("It's quiter than on the cementery.")
elif noise == 40:
    print("It's the quiet room sound level.")
elif noise > 40 < 70:
    print("It's between quiet room and an alarm clock level.")
elif noise == 70:
    print("It's an alarm clock sound level.")
elif noise > 70 < 106:
    print("Right between alarm clock and gas lawnmower sound level.")
elif noise == 106:
    print("Lawnmower level.")
elif noise > 106 < 130:
    print("Between gas lawnmower and jackhammer.")
elif noise == 130:
    print("Jackhammer's sound level.")
else:
    print("This is just above the norm. Louder than a jackhammer!")



#Version 2
def sound_level():
    noise = int(input('Enter the sound level in decibels (134 to quit): '))
    while True:
        if noise == 134:
            break
        elif noise < 40:
            print("It's quiter than on the cementery.")
        elif noise == 40:
            print("It's the quiet room sound level.")
        elif noise > 40 and noise < 70:
            print("It's between quiet room and an alarm clock level.")
        elif noise == 70:
            print("It's an alarm clock sound level.")
        elif noise > 70 and noise < 106:
            print("Right between alarm clock and gas lawnmower sound level.")
        elif noise == 106:
            print("Lawnmower level.")
        elif noise >106 and noise < 130:
            print("Between gas lawnmower and jackhammer.")
        elif noise == 130:
            print("Jackhammer's sound level.")
        elif noise > 130 and noise != 134:
            print("This is just above the norm. Louder than a jackhammer!")

        noise = int(input('Enter the sound level in decibels (134 to quit): '))

sound_level()    
