import shelve
ar=shelve.open('ar_words.txt')
ra=shelve.open('ra_words.txt')

# Functions for translation

def translation_of_adi():
    adi_in_rus=input('Enter an Adifiro word: ')
    if adi_in_rus in ar:
        print(ar.get(adi_in_rus))
    else:
        print('Word not found')

translation_of_adi()

def translation_of_rus():
    rus_in_adi=input('Enter a russian word: ')
    if rus_in_adi in ra:
        print(ra.get(rus_in_adi))
    else:
        print('Word not found')

translation_of_rus()

# Functions for adding words

def add_adi_rus():
    new_adi_ar=input('Add an Adifiro word: ')
    new_rus_ar=input('Add a russian word: ')
    ar[new_adi_ar]=new_rus_ar
    print('New word is added')
    print('Renewed Adifiro-russian dictionary: ', ar)
    ar.update()
    ar.close()

add_adi_rus()

def add_rus_adi():
    new_rus_ra=input('Add a russian word: ')
    new_adi_ra=input('Add an Adifiro word: ')
    ra[new_rus_ra]=new_adi_ra
    print('New word is added')
    print('Renewed russian-Adifiro dictionary: ', ra)
    ra.update()
    ra.close()

add_rus_adi()

print(dict(ar.items()))
print(dict(ra.items()))