#v1(output without details)

def bodyMassIndex():
    height = float(input('Enter your height in meters: '))
    weight = float(input('Enter your weight in kilograms: '))
    bmi = weight / (height * height)

    print('Your BMI is ', bmi)

bodyMassIndex()

#v2
def bodyMassIndex(height, weight):
    bmi = weight / (height * height)

    print('Your BMI is ', bmi)

    if 18.5 < bmi < 25:
        print('Normal weight')
    elif 25 < bmi < 30:
        print('Overweight')
    elif bmi > 30:
        print('Obese')
    else:
        print('Underweight')


bodyMassIndex(1.78,60)
bodyMassIndex(1.70,60)
bodyMassIndex(1.73,57)

#v3
def bodyMassIndex(height, weight):
    bmi = round(weight / (height * height),2)

    print('Your BMI is ', bmi)

    if 18.5 < bmi < 25:
        print('Normal weight')
    elif 25 < bmi < 30:
        print('Overweight')
    elif bmi > 30:
        print('Obese')
    else:
        print('Underweight')


bodyMassIndex(1.78,60)
bodyMassIndex(1.70,60)
bodyMassIndex(1.73,57)

#v4 (with details)
def bodyMassIndex():
    height = float(input('Enter your height in meters: '))
    weight = float(input('Enter your weight in kilograms: '))
    bmi = round(weight / (height * height))

    print('Your BMI is ', bmi)

    if bmi in range(0, 20):
        print('This is the body mass deficit.')
    elif bmi in range(20, 26):
        print('This is a normal weight.')
    elif bmi in range(25, 31):
        print('It is one phase before obesity, please start dieting and sports.')
    else:
        print('Obesity is not healthy. Try sports and dieting.')

#v5
bodyMassIndex()
def bodyMassIndex(height, weight):
    bmi = round(weight / (height * height))

    print('Your BMI is ', bmi)

    if bmi in range(0, 20):
        print('This is the body mass deficit.')
    elif bmi in range(20, 26):
        print('This is a normal weight.')
    elif bmi in range(25, 31):
        print('It is one phase before obesity, please start dieting and sports.')
    else:
        print('Obesity is not healthy. Try sports and dieting.')

bodyMassIndex(1.78,60)
bodyMassIndex(1.70,60)
bodyMassIndex(1.73,57)