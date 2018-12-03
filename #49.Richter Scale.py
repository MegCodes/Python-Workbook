while True:
    quacke = 'earthquake'
    magnitude = float(input("Please enter the earthquacke's magnitude (20 to quit): "))
    if magnitude == 20:
        break
    elif magnitude > 0 and magnitude < 2:
        print('It is a micro', quacke)
    elif magnitude >= 2 and magnitude < 3:
        print('It is a very minor', quacke)
    elif magnitude >= 3 and magnitude < 4:
        print('It was a minor', quacke)
    elif magnitude >= 4 and magnitude < 5:
        print('It is a light', quacke)
    elif magnitude >=5 and magnitude < 6:
        print('It is a moderate', quacke)
    elif magnitude >=6 and magnitude < 7:
        print('It is a strong', quacke)
    elif magnitude >= 7 and magnitude < 8:
        print("It is a major", quacke)
    elif magnitude >= 8 and magnitude < 10:
        print("It is a great", quacke)
    else:
        print("It is a meteoric", quacke)

