#Импорт
from tkinter import * # Графический интерфейс
from time import strftime # Для работы с временем
import tkinter.messagebox as mb # Для всплывающих окон (Именно для showerror)
#Код

#Картинка для фона
#Ссылка - https://wallpapershome.ru/images/wallpapers/samolet-3840x2160-minimalizm-18613.jpg Последнее время обращения: указать дату

#Иконка для приложения
#Ссылка - #https://icon-icons.com/ru/значок/часы/102733 Последнее время обращения: указать дату


#Создание окна
main_root = Tk()

#Название приложения
main_root.title('Конвертер Времени')

#Иконка приложения
main_root.iconbitmap('Иконка для приложения_.ico')

#Размеры окна
main_root.geometry("300x300+100+100")

#Нельзя изменять размеры
main_root.resizable(width = False, height = False)

#Шапка приложения
image_main_root = PhotoImage(file = 'Фон.png') #300x300 Для окна без истории, 300х600 Для окна с историей
label_main_root_image = Label(main_root, image = image_main_root)
label_main_root_image.pack(side = TOP)


#Поле для ввода
label_bg_e = Label(main_root, bg = '#77BDE4')
label_bg_e.place(x = 5, y = 165, height = 40, width = 130)
main_entry = Entry(main_root, justify = 'center', bd = '0', bg = '#20329B', fg = '#77BDE4', font = '30')
main_entry.place(x = 7, y = 167, height = 36, width = 126)
#Установка фокуса
#main_entry.focus_set() - пока не нужно)))

#Поле для вывода информации
label_bg_f = Label(main_root, bg = '#77BDE4').place(x = 5, y = 95, height = 40, width = 290)
entry_f = Entry(main_root, justify = 'center', bd = '0', bg = '#20329B', fg = '#77BDE4', font = '30')
entry_f.place(x = 7, y = 97, height = 36, width = 286)

#Текстовое поле, для отображения
label_t = Label(main_root, bg = '#77BDE4').place(x = 305, y = 5, height = 130, width = 290)
text_info = Text(main_root, bg = '#20329B', fg = '#77BDE4', bd = '0', font = '30')
text_info.place(x = 307, y = 7, height = 126, width = 286)

#Массивы

#Массив для переключения типа конвертации
array_type = []

#Функции тута

#Функция - 'Фоновый текст' 2 шт для entry 'Ввода' и 'Вывода'
placeholder_s = 'ВВОД' #Фоновый текст
def del_placeholder_s(event = None): 
	if main_entry.get() == placeholder_s: #Если текст в entry совпадает с фоновым, то удаляем содержимое entry
		main_entry.delete(0, END) 
def add_placeholder_s(event = None):
	if main_entry.get() == '': #Если в entry нет текста, то устанавливаем туда фоновый текст
		main_entry.insert(0, placeholder_s)
add_placeholder_s() #Автозапуск Фонового текста
main_entry.bind('<FocusIn>', del_placeholder_s) #При клике на entry текст будет удаляться 
main_entry.bind('<FocusOut>', add_placeholder_s) #При расфокусировке entry текст будет появляться, если entry пустое
#
placeholder_f = 'ВЫВОД' #Фоновый текст
def del_placeholder_f(event = None):
	if entry_f.get() == placeholder_f: #Если текст в entry совпадает с фоновым, то удаляем содержимое entry
		entry_f.delete(0, END)
def add_placeholder_f(event = None):
	if entry_f.get() == '': #Если в entry нет текста, то устанавливаем туда фоновый текст
		entry_f.insert(0, placeholder_f)
add_placeholder_f() #Автозапуск Фонового текста
entry_f.bind('<FocusIn>', del_placeholder_f) #При клике на entry текст будет удаляться 
entry_f.bind('<FocusOut>', add_placeholder_f) #При расфокусировке entry текст будет появляться, если entry пустое
	
#Запись истории
global info_txt #Чтобы достучаться из любого места
def info_txt(): 
	text_info.delete(1.0, END) #Очищаем текст, чтобы небыло информационной 'Каши'
	with open('information.txt','r') as info_file:
		#Чтение файла
		text = info_file.readlines() #Читаем файл целиком
		text = ''.join(text) #Соединяем строки
		text_info.insert(1.0, text) #Вывод информации в текстовое поле
info_txt() #Автозапуск

#Очистить историю
def clear_info():
	#Предупредить пользователя, что он хочет очистить историю и попросить подтверждения этого действия
	msg = 'Удалить историю?'
	answer = mb.askyesno('Подтверждение действия', msg)
	if answer: #answer принимает два значения - 'True' и 'False': Если правда, то выполняет действие, если ложь, то ничего не произойдет
		open('information.txt', 'w+').close() #Открываем и сразу же закрываем файл с 'w+' - это удалит все содержимое файлика
		info_txt() #Запуск функции вставки текста, чтобы визуализировать отсутствие информации в файлике

#Функция - 'Дни в Минуты'
def days_in_minutes():
	#Заблокировать Кнопочку - 'Дни в Минуты'
	button_d_m['state'] = 'disabled'
	#Разблокировать Кнопочку - 'Минуты в Дни'
	button_m_d['state'] = 'normal'

	#Очистить массив(array_type) и поставить значение - '0'
	array_type.clear()
	array_type.append(0)

#Функция - 'Минуты в Дни'
def minutes_in_days():
	#Заблокировать Кнопочку - 'Минуты в Дни'
	button_m_d['state'] = 'disabled'
	#Разблокировать Кнопочку - 'Дни в Минуты'
	button_d_m['state'] = 'normal'

	#Очистить массив(array_type) и поставить значение - '1'
	array_type.clear()
	array_type.append(1)

#Функция - 'Показать историю'
def open_txt():
	#Если кнопочка называется - 'Показать историю', то
	#Меняем параметры под большое окно
	#Если кнопочка называется - 'Скрыть историю', то
	#Меняем параметры под маленькое окно

	if button_open_txt['text'] == 'Показать Историю':

		#Увеличиваем размер приложения
		main_root.geometry("600x300")

		#Изменяем положение кнопочки - 'Показать историю' + Изменяем её название на - 'Скрыть историю'
		label_bg_o.place(x = 305, y = 255, height = 40, width = 290)
		button_open_txt.place(x = 307, y = 257, height = 36, width = 286)
		button_open_txt['text'] = 'Скрыть Историю'

		#Изменяем положение кнопочки - 'Конвертировать'
		label_bg_s.place(x = 5, y = 255, height = 40, width = 290)
		button_start.place(x = 7, y = 257, height = 36, width = 286)

		#Изменяем положение текстового поля для ввода данных
		label_bg_e.place(x = 5, y = 210, height = 40, width = 130)
		main_entry.place(x = 7, y = 212, height = 36, width = 126)

		#Изменяем положение кнопочки - 'Об Авторе'
		label_bg_i.place(x = 140, y = 210, height = 40, width = 155)
		button_info.place(x = 142, y = 212, height = 36, width = 151)

	elif button_open_txt['text'] == 'Скрыть Историю':

		#Уменьшаем размер приложения
		main_root.geometry("300x300")

		#Изменяем положение кнопочки - 'Скрыть историю' + Изменяем её название на - 'Показать историю'
		label_bg_o.place(x = 5, y = 255, height = 40, width = 290)
		button_open_txt.place(x = 7, y = 257, height = 36, width = 286)
		button_open_txt['text'] = 'Показать Историю'

		#Изменяем положение кнопочки - 'Конвертировать'
		label_bg_s.place(x = 5, y = 210, height = 40, width = 290)
		button_start.place(x = 7, y = 212, height = 36, width = 286)

		#Изменяем положение текстового поля для ввода данных
		label_bg_e.place(x = 5, y = 165, height = 40, width = 130)
		main_entry.place(x = 7, y = 167, height = 36, width = 126)

		#Изменяем положение кнопочки - 'Об Авторе'
		label_bg_i.place(x = 140, y = 165, height = 40, width = 155)
		button_info.place(x = 142, y = 167, height = 36, width = 151)

#Функция - 'Об Авторе' будет запускаться при наведении на кнопочку - 'Об Авторе'
def author_info_on(event):
	#Создаем label
	global label_bg_info, label_info
	label_bg_info = Label(main_root, bg = '#77BDE4')
	label_bg_info.place(x = 5, y = 5, height = 130, width = 290)
	
	label_info = Label(main_root, bg = '#20329B', 
		text = '(c) Федоров Максим Алексеевич\n*****\n' +
		'Эл. Почта: fedorowma@yandex.ru\n*****\n23 Ноября 2021 г.', 
		fg = '#77BDE4', font = '12')
	label_info.place(x = 7, y = 7, height = 126, width = 286)
def author_info_off(event):
	#Создаем label
	label_bg_info.place_forget() #Скрываем виджет
	label_info.place_forget() #Скрываем виджет
	
#Функция - 'Конвертировать'
def start_programm():
	#Проверка на выбор варианта конвертации, если пользователь не выбрал, выдать предупреждение
	len_array = len(array_type) #Узнаём длинну массива
	if len_array == 1: #Дни в минуты
		if array_type[0] == 0:
			try:
				days = float(main_entry.get())
				minutes = days * 1440
				entry_f.delete(0, END)
				#Вывод
				entry_f.insert(0, round(minutes, 5)) #rоund - округление
				#Время
				time = strftime("%H:%M:%S") #Часы, Минуты, Секунды
				#Запись в историю
				time = str(time) + ' | ' + str(round(days, 5)) + ' Д. = ' + str(round(minutes, 5)) + ' Мин.' #rоund - округление
				with open('information.txt','a+') as info_file:
					info_file.write(time + '\n') #Вставка текста + 'переноска' на следующую строку
				info_txt() #Запуск функции вставки текста
			except:
				#Выдает ошибку, так как необходимо использовать числа
				msg = 'Можно вводить только числа.\nНапример:\n2, 5, 0.5, и т.п.'
				mb.showinfo('Информация', msg) 
		elif array_type[0] == 1: #Минуты в дни
			try:
				minutes = float(main_entry.get())
				days = minutes / 1440
				entry_f.delete(0, END)
				#Вывод
				entry_f.insert(0, round(days, 5)) #rоund - округление
				#Время
				time = strftime("%H:%M:%S") #Часы, Минуты, Секунды
				#Запись в историю
				time = str(time) + ' | ' + str(round(minutes, 5)) + ' Мин. = ' + str(round(days, 5)) + ' Д.' #rоund - округление
				with open('information.txt','a+') as info_file:
					info_file.write(time + '\n') #Вставка текста + 'переноска' на следующую строку
				info_txt() #Запуск функции вставки текста
			except:
				#Выдает ошибку, так как необходимо использовать числа
				msg = 'Можно вводить только числа.\nНапример:\n2, 5, 0.5, и т.п.'
				mb.showinfo('Информация', msg) 
	else:
		msg = 'Выберите тип конвертации'
		mb.showinfo('Информация', msg)
#Добавим красоты

#Создание функции изменения цвета при наведении
def on_button_color(event):
	event.widget['bg'] = '#233BC8'
	event.widget['fg'] = '#77BDE4'
def off_button_color(event):
	event.widget['bg'] = '#20329B'
	event.widget['fg'] = '#77BDE4'

#Кнопочки

#Кнопочка - 'Конвертировать'
label_bg_s = Label(main_root, bg = '#77BDE4')
label_bg_s.place(x = 5, y = 210, height = 40, width = 290)
button_start = Button(main_root, bg = '#20329B', text = 'Конвертировать', fg = '#77BDE4', 
	font = '12', bd = '0', activebackground = '#333FEB', command = start_programm)
button_start.place(x = 7, y = 212, height = 36, width = 286)
#
button_start.bind("<Enter>", on_button_color)
button_start.bind("<Leave>", off_button_color)

#Кнопочка - 'Показать Историю' она же - 'Скрыть Историю'
label_bg_o = Label(main_root, bg = '#77BDE4')
label_bg_o.place(x = 5, y = 255, height = 40, width = 290)
button_open_txt = Button(main_root, bg = '#20329B', text = 'Показать Историю', fg = '#77BDE4',
	font = '12', bd = '0', activebackground = '#333FEB', command = open_txt)
button_open_txt.place(x = 7, y = 257, height = 36, width = 286)
#
button_open_txt.bind("<Enter>", on_button_color)
button_open_txt.bind("<Leave>", off_button_color)

#Кнопочка - 'Об Авторе'
label_bg_i = Label(main_root, bg = '#77BDE4')
label_bg_i.place(x = 140, y = 165, height = 40, width = 155)
button_info = Button(main_root, bg = '#20329B', text = 'Об Авторе', fg = '#77BDE4',
	font = '12', bd = '0', activebackground = '#333FEB')
button_info.place(x = 142, y = 167, height = 36, width = 151)
#
button_info.bind("<Enter>", lambda event: [on_button_color(event), author_info_on(event)])
button_info.bind("<Leave>", lambda event: [off_button_color(event), author_info_off(event)])

#Кнопочки для выбора типа конвертации

#Кнопочка - 'Дни в Минуты'
label_bg_d_m = Label(main_root, bg = '#77BDE4')
label_bg_d_m.place(x = 5, y = 5, height = 40, width = 290)
button_d_m = Button(main_root, bg = '#20329B', text = 'Дни в Минуты', fg = '#77BDE4',
	font = '12', bd = '0', activebackground = '#333FEB', command = days_in_minutes)
button_d_m.place(x = 7, y = 7, height = 36, width = 286)
#
button_d_m.bind("<Enter>", on_button_color)
button_d_m.bind("<Leave>", off_button_color)

#Кнопочка - 'Минуты в Дни'
label_bg_m_d = Label(main_root, bg = '#77BDE4')
label_bg_m_d.place(x = 5, y = 50, height = 40, width = 290)
button_m_d = Button(main_root, bg = '#20329B', text = 'Минуты в Дни', fg = '#77BDE4',
	font = '12', bd = '0', activebackground = '#333FEB', command = minutes_in_days)
button_m_d.place(x = 7, y = 52, height = 36, width = 286)
#
button_m_d.bind("<Enter>", on_button_color)
button_m_d.bind("<Leave>", off_button_color)

#Кнопочка - 'Очистить Историю'
label_bg_clear = Label(main_root, bg = '#77BDE4')
label_bg_clear.place(x = 305, y = 210, height = 40, width = 290)
button_clear = Button(main_root, bg = '#20329B', text = 'Очистить Историю', fg = '#77BDE4',
	font = '12', bd = '0', activebackground = '#333FEB', command = clear_info)
button_clear.place(x = 307, y = 212, height = 36, width = 286)
#
button_clear.bind("<Enter>", on_button_color)
button_clear.bind("<Leave>", off_button_color)

#Потому, что да
main_root.mainloop()