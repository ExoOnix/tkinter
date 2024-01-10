from tkinter import *
from random import randint
root = Tk()
root.title('Sticks')
root.geometry('400x300')
root.resizable(height=False, width=False)
sticks = 20
label_move = Label(text='Type a number from 1 to 3', font='Arial 15 bold')
entry_sticks = Entry(font='Arial 15 bold')
entry_sticks.focus()
status = Label(text=sticks, font='Arial 30 bold')
def player():
	global sticks
	delete_sticks = int(entry_sticks.get())
	if (delete_sticks in [1, 2, 3]) and (sticks >= delete_sticks):
		sticks -= delete_sticks
		entry_sticks.delete(0, END)
		label_sticks.config(text=sticks*'|')
		status.config(text=sticks)
		if sticks == 1:
			status.config(text='You won', fg='Green')
		else:
			label_move.config(text='Computers turn')
			entry_sticks.config(state=DISABLED)
			root.after(2000, computer)
def computer():
	global sticks, cdelete_sticks
	cdelete_sticks = randint(1, 3)
	if sticks <= 4:
		cdelete_sticks = sticks -1
	sticks -= cdelete_sticks
	label_sticks.config(text=sticks*'|')
	status.config(text=sticks)
	if sticks == 1:
		status.config(text='The bot won')
	else:
		label_move.config(text='Type a number from 1 to 3')
		entry_sticks.config(state=NORMAL)



label_sticks = Label(text=sticks*'|', font='Arial 30 bold')
button = Button(text='Take sticks', font='Arial 15 bold', command=player)


label_move.pack()
entry_sticks.pack()
label_sticks.pack()
status.pack()
button.pack()
root.mainloop()
