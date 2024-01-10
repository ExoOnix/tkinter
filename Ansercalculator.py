from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('550x300')
root.title('Question calculator')
root.resizable(height=False, width=False)

def equate():
	try:
		solution = eval(equation.get())
		messagebox.showinfo('Fineshed', f'Anser is found: {solution}')
	except (NameError):
		messagebox.showerror('Error', 'Something went wrong')
	except (ZeroDivisionError):
		messagebox.showinfo('Info', 'Cannot divide by 0')
	except (SyntaxError):
		messagebox.showwarning('Warning', 'Retry')
frame = Frame(width=550, height=80)
label = Label(text='Enter a mathmatic entry using the simbols + - * / // % **')
equation = Entry(width=40)
equation.focus()
button = Button(text='Check!', height=2, width=20, command=equate)


frame.pack()
label.pack()
equation.pack(pady=5)
button.pack(pady=5)

root.mainloop()