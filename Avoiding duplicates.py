words = []
word = input('Enter a word (space to quit): ')
while word !=' ':
    if word not in words:
        words.append(word)
        words = input('Enter a word (space to quit): ')
print('So the input is: ')

for word in words:
    print(word)