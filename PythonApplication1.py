from tkinter import *
# подключаем tkinter
from tkinter.messagebox import *
# подключаем диалоговые окна tkinter
root = Tk( ) # создаем главное окно
# Устанавливаем минимальные и максимальные размеры окна:
root.minsize(width = 350, height = 150)
root.maxsize(width = 550, height = 300)
root.title("Калькулятор") # заголовок окна
# Создадим 3 фрейма: fr_xy, fr_op и fr_res для размещения компонент.
fr_xy = Frame(root)
# фрейм fr_xy (компоненты для ввода чисел x, y).
fr_xy.pack(side = TOP, expand = YES, fill = X)
# На нем размещаем две метки и два редактора для ввода чисел x, y:
lx = Label(fr_xy, background="white", foreground="blue", text = "x = ")
lx.pack(side = LEFT, padx = 10, pady = 10)
entX = Entry(fr_xy, background="white", foreground="blue")
entX.insert(0, 0)
# – в редактор записываем в позицию 0 число 0
entX.pack(side = LEFT, padx=10, pady=10)
entX.focus( )
# – редактор будет выбран при старте (иметь фокус ввода)
ly = Label(fr_xy, background="white", foreground="green", text = "y = ")
ly.pack(side=LEFT, padx=10, pady=10)
entY = Entry(fr_xy, background="white", foreground="green")
entY.insert(0, 0)
entY.pack(side = LEFT, padx=10, pady=10)
# Создание фрейма с заголовком fr_op (выбор операции):
fr_op = LabelFrame(root, text = "Операция:", background="gray")
fr_op.pack(side = TOP, expand=YES, fill=X)
# Операцию будем выбирать с помощью виджета Radiobutton:
oper = ['+', '-', '*', '/', '%', '//', "**"] # – список операций
# Вводим строковую переменную tkinter, ее свяжем с выбором Radiobutton
varOper = StringVar( )
i=0
# В цикле создаем 7 кнопок Radiobutton (связываем их с переменной):
for op in oper:
	Radiobutton(fr_op, background="darkgray", foreground="blue", text = op, variable = varOper, value = op).pack(side = LEFT, padx = 20, pady = 10)
	varOper.set(oper[0]) # Устанавливаем текущее значение ‘+’

# Создаем 3-й фрейм fr_res (вычисление значения и вывод результата):
fr_res = Frame(root)
fr_res.pack(side = TOP, expand = YES, fill = BOTH)
acts = []
# Обработчик кнопки:
def OnButtunResult( ):# Защищенный блок, будем пытаться перевести текст из редактора в число:
	try:
		x = float(entX.get())
# извлекаем число из 1-го редактора
	except ValueError:# если не получилось, выдаем сообщение и выходим
		showerror("Ошибка заполнения", "Переменная x не является числом")
		return # Защищенный блок 2:
	try:
		y = float(entY.get())
	except ValueError:
		showerror("Ошибка заполнения", "Переменная y не является числом")
		return

# В переменную op записываем выбранную операцию:

	op = varOper.get( )
# Вычисляем:
	if op == '+': res = x + y
	elif op == '-': res = x - y
	elif op == '*': res = x * y
	elif op == '**': res = x ** y
	elif op == '/':
		if y != 0: res = x / y
		else: res = 'NAN'
	elif op == '%':
		if y != 0: res = x % y
		else: res = 'NAN'
	elif op == '//':
		if y != 0: res = x // y
		else: res = 'NAN'
	else:
		res = 'операция выбрана неправильно'

# Вывод результата на метку:
	acts.append(res) # Обработчик кнопки закончился.
	lb.insert(END, res)
	# Создаем кнопку и метку, к кнопке присоединяем обработчик:
w = Button(fr_res, text = "=", background="#555", foreground="#ccc", width = 10, command = OnButtunResult)
# задаем вид курсора мыши над виджетом:
w.config(cursor = "cross")
w.pack(side = LEFT, padx = 30, pady = 20)

lb = Listbox(fr_res, height = 5)
scrollbar = Scrollbar(fr_res)
scrollbar.pack(side = LEFT, fill = Y)
for i in acts:
	lb.insert(END, i)
	lb.pack(pady=15)
lb.config(yscrollcommand = scrollbar.set) 
lb.pack(side = LEFT, padx = 30, pady = 20)
scrollbar.config(command=lb.yview)

# Запуск цикла обработки сообщений:
root.mainloop( )
