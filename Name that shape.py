def name_shape():
    print('I will try to name the shapes based on number of their sides, as entered by you.\
Please enter number of sides from 3 to 10.')
    sides = int(input('Number of sides(55 to quit): '))
    while True:
        if sides == 55:
            break
        elif sides < 3 or sides > 10:
            print('Number should be from 3 to 10.')
            sides = int(input('Number of sides(55 to quit): '))
        if sides == 3:
            print('Triangle')
        elif sides == 4:
            print('Quadrilateral')
        elif sides == 5:
            print('Pentagon')
        elif sides == 6:
            print('Hexagon')
        elif sides == 7:
            print('Heptagon')
        elif sides == 8:
            print('Octagon')
        elif sides == 9:
            print('Nonagon')
        elif sides == 10:
            print('Decagon')
        sides = int(input('Number of sides(55 to quit): '))


name_shape()