from tkinter import *
from random import *
root = Tk()
root.title('Random Name Picker')
root.geometry('220x150')
root.resizable(width=False, height=False)
def NAMEGEN():
	n = name_input.get()
	names = n.split(', ')
	f = choice(names)
	lb_2.config(text=f)

lb_1 = Label(text='Random Name Picker', font='Arial 12', fg='black', bg='white', width=25, height=2)
name_input = Entry(width=30)
lb_2 = Label(text='', font='Arial 10', fg='black', bg='white', width=25, height=1)
btn1 = Button(text='Start', height=1, width=15, justify=CENTER, command=NAMEGEN)



lb_1.grid(row=0, column=0, columnspan=3)
name_input.grid(row=1, column=0, columnspan=3, pady=5)
btn1.grid(row=2, column=0, columnspan=3, pady=4)
lb_2.grid(row=3, column=0, columnspan=3, pady=4)
root.mainloop()