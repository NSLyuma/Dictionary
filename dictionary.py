from ar_words import ar

def adi():
    adi_words=dict([[v, k] for k,v in ar.items()])
    find_word=input('Enter a russian word: ' '')
    print(adi_words.get(find_word) or print('Word not found'))
    return adi()

def rus():
    rus_words=dict([[k, v] for k,v in ar.items()])
    find_word=input('Enter an Adifiro word: ' '')
    print(rus_words.get(find_word) or print('Word not found'))
    return rus()

user_input=input('Enter:\n-a to input an Adifiro word\n-r to input a russian word\n')
command=user_input[0]
while True:
    if command=='r':
        print(adi())
    elif command=='a':
        print(rus())
    else:
        print('Incorrect command')
        break
print(user_input)