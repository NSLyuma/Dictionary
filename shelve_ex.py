import shelve
# ar=shelve.open('ar_words.txt') #открываю словарь
# ar['enie']='а,','и (сложное)' #добавляю новое значение в словарь
# print(dict(ar.items())) #выводит весь словарь
# ar.close()

# Удалить значение из словаря
# ra=shelve.open('ra_words.txt')
# ra.pop('а, и (сложное)','enie')
# print(dict(ra.items()))
# ra.close()

# Вывести упорядоченный словарь
# ar=shelve.open('ra_words.txt')
# list_ar=list(ar.keys())
# list_ar.sort()
# for i in list_ar:
#     print(i,'-',ar[i])
# ar.close()