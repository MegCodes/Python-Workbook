chars = ['.',',',':',';','&','!','?','@','\\','|','/',' ']


while True:
    word = input("Please enter a word (q to quit): ").lower()
    for char in word:
        if char in chars:
            word = word.replace(char, '')

    if word == '' or word == ' ':
        print('There should be a value.')
    elif word == 'q':
        break
    else:
        check = word[::-1]
        if check == word:
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")


