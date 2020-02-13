from tkinter import *

# Создаём окно
window=Tk()
window.title('Russian-Adifiro/Adifiro-Russian translator')
# Настройка размеров окна приложения
window.geometry('400x500')

# Раздел перевода слов
# Название
title1=Label(text='Translator')
title1.place(x=200, y=10, anchor=CENTER)
# Названия полей для ввода слов
enter_rus=Label(window, text='Enter a russian word')
enter_adi=Label(window, text='Enter an Adifiro word')
enter_rus.place(x=70, y=40, anchor=CENTER)
enter_adi.place(x=330, y=40, anchor=CENTER)
# # Поля для ввода текста
rus_word_tr=Entry()
adi_word_tr=Entry()
rus_word_tr.place(x=70, y=60, anchor=CENTER)
adi_word_tr.place(x=330, y=60, anchor=CENTER)
# Кнопка для перевода слов
translate_button=Button(text='Translate') #Add function
translate_button.place(x=200, y=60, anchor=CENTER)
# Поля для вывода перевода слов
rus_tr=Label(text='Russian translation', fg='grey')
adi_tr=Label(text='Adifiro translation', fg='grey')
rus_tr.place(x=70, y=80, anchor=CENTER)
adi_tr.place(x=330, y=80, anchor=CENTER)

# Раздел добавления слов
# Название
title2=Label(text='Add new words')
title2.place(x=200, y=120, anchor=CENTER)
# # Примечание
note=Label(text='Note: If you want to add one russian word with several Adifiro meanings,\npress \'Add in russian\'. Otherwise press \'Add in Adifiro.', fg='brown')
note.place(x=0, y=150, anchor=W)
# Названия полей для ввода слов
add_rus=Label(window, text='Enter a russian word')
add_adi=Label(window, text='Enter an Adifiro word')
add_rus.place(x=70, y=180, anchor=CENTER)
add_adi.place(x=330, y=180, anchor=CENTER)
# Поля для ввода текста
rus_word_ad=Entry()
adi_word_ad=Entry()
rus_word_ad.place(x=70, y=200, anchor=CENTER)
adi_word_ad.place(x=330, y=200, anchor=CENTER)
# Кнопки для добавления новых слов
add_both_button=Button(text='Add both') #Add commands
add_in_rus_button=Button(text='Add in russian')
add_in_adi_button=Button(text='Add in Adifiro')
add_both_button.place(x=200, y=200, anchor=CENTER)
add_in_rus_button.place(x=70, y=230, anchor=CENTER)
add_in_adi_button.place(x=330, y=230, anchor=CENTER)

# Последняя строка вызывает функцию mainloop. Эта функция вызывает бесконечный цикл окна, поэтому окно будет ждать
# любого взаимодействия с пользователем, пока не будет закрыто
# В случае, если вы забудете вызвать функцию mainloop, для пользователя ничего не отобразится
window.mainloop()