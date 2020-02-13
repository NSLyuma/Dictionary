from tkinter import *
import shelve
ar=shelve.open('ar_words.txt')
ra=shelve.open('ra_words.txt')

# -------------------Блок функций-------------------

# Функция для перевода слов
def translate():
    user_word=rus_word_tr.get()
    if user_word in ra:
        adi_tr.config(text=ra[user_word], fg='blue')
    rus_word_tr.delete(0, 'end')

    if user_word not in ra:
        adi_tr.config(text='')

    user_word=adi_word_tr.get()
    if user_word in ar:
        rus_tr.config(text=ar[user_word], fg='blue')
    adi_word_tr.delete(0, 'end')

    if user_word not in ar:
        rus_tr.config(text='')

# Функции для добавления новых слов
def add_both_word():
    new_word_rus=rus_word_ad.get()
    new_word_adi=adi_word_ad.get()
    ra[new_word_rus]=new_word_adi
    ar[new_word_adi]=new_word_rus
    ra.update()
    ar.update()
    # message_label.config(text='Words successfully added!', fg='green')
    rus_word_ad.delete(0, 'end')
    adi_word_ad.delete(0, 'end')

def add_in_rus():
    new_word_rus = rus_word_ad.get()
    new_word_adi = adi_word_ad.get()
    ra[new_word_rus] = new_word_adi
    ra.update()
    rus_word_ad.delete(0, 'end')
    adi_word_ad.delete(0, 'end')

def add_in_adi():
    new_word_adi = adi_word_ad.get()
    new_word_rus = rus_word_ad.get()
    ar[new_word_adi]=new_word_rus
    ar.update()
    rus_word_ad.delete(0, 'end')
    adi_word_ad.delete(0, 'end')

# -------------------Конец блока функций-------------------

# -------------------Блок графического интерфейса-------------------

# Создаём окно
window=Tk()
window.title('Russian-Adifiro/Adifiro-Russian translator')
# Настройка размеров окна приложения
window.geometry('336x300')

# Раздел перевода слов
# Название
title1=Label(text='Translator')
title1.grid(column=1, row=0)
# Названия полей для ввода слов
enter_rus=Label(window, text='Enter a russian word')
enter_adi=Label(window, text='Enter an Adifiro word')
enter_rus.grid(column=0, row=1)
enter_adi.grid(column=2, row=1)
# Поля для ввода текста
rus_word_tr=Entry()
adi_word_tr=Entry()
rus_word_tr.grid(column=0, row=2)
adi_word_tr.grid(column=2, row=2)
# Кнопка для перевода слов
translate_button=Button(text='Translate', command=translate)
translate_button.grid(column=1, row=2)
# Поля для вывода перевода слов
rus_tr=Label(text='Russian translation', fg='grey')
adi_tr=Label(text='Adifiro translation', fg='grey')
rus_tr.grid(column=0, row=3)
adi_tr.grid(column=2, row=3)

# Раздел добавления слов
# Название
title2=Label(text='Add new words')
title2.grid(column=1, row=4)
# Примечание
note1=Label(text='Note: If you want to add one russian word with several Adifiro', fg='brown')
note2=Label(text='meanings, press \'Add in russian\'. Otherwise press \'Add in', fg='brown')
note3=Label(text='Adifiro.', fg='brown')
# Пустые поля, чтобы на их место поставить примечание
note1.place(x=0, y=110)
note2.place(x=0, y=130)
note3.place(x=0, y=150)
empty1=Label(text='')
empty2=Label(text='')
empty3=Label(text='')
empty1.grid(column=3, row=5)
empty2.grid(column=3, row=6)
empty3.grid(column=3, row=7)
# Названия полей для ввода слов
add_rus=Label(window, text='Enter a russian word')
add_adi=Label(window, text='Enter an Adifiro word')
add_rus.grid(column=0, row=8)
add_adi.grid(column=2, row=8)
# Поля для ввода текста
rus_word_ad=Entry()
adi_word_ad=Entry()
rus_word_ad.grid(column=0, row=9)
adi_word_ad.grid(column=2, row=9)
# Кнопки для добавления новых слов
add_both_button=Button(text='Add both', command=add_both_word)
add_in_rus_button=Button(text='Add in russian', command=add_in_rus)
add_in_adi_button=Button(text='Add in Adifiro', command=add_in_adi)
add_both_button.grid(column=1, row=9)
add_in_rus_button.grid(column=0, row=10)
add_in_adi_button.grid(column=2, row=10)
# Поле для вывода сообщений
# message_label=Label(text='Words successfully added!')
# message_label.place(x=90, y=160)

# Последняя строка вызывает функцию mainloop. Эта функция вызывает бесконечный цикл окна, поэтому окно будет ждать
# любого взаимодействия с пользователем, пока не будет закрыто
# В случае, если вы забудете вызвать функцию mainloop, для пользователя ничего не отобразится
window.mainloop()

# -------------------Конец блока графического интерфейса-------------------

print(dict(ar.items()))
print(dict(ra.items()))

ra.close()
ar.close()

# Сделать возможность добавления слов отдельно в русско-Адифиро и отдельно в Адифиро-русский словари, когда у одного
# слова несколько значений.
# Надо всё-таки додумать штуку, чтобы если слова нет в словаре, он НОРМАЛЬНО выводил Word not found.
# Как-то надо сделать, чтобы русский перевод стирался, когда вылезает Адифиро и наоборот.
# Сделать вкладки, чтобы в первой был переводчик и добавитель слов, во второй список Адифиро-русских слов, а в третьей -
# русско-Адифиро слов, которые уже добавлены в словарь. И надо, чтобы в каждом словаре слова были в алфавитном порядке.

# Add in russian Add in Adifiro
# Note: If you want to add one russian word with several Adifiro meanings, press 'Add in russian'. Otherwise press 'Add in Adifiro'.