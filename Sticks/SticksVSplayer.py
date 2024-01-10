from tkinter import *
root = Tk()
root.title('Sticks')
root.geometry('400x300')
root.resizable(height=False, width=False)
sticks = 20
label_move = Label(text='Player 1, type a number from 1 to 3', font='Arial 15 bold')
entry_sticks = Entry(font='Arial 15 bold')
status = Label(text=sticks, font='Arial 30 bold')
counter = 0
def player():
	global sticks, counter
	delete_sticks = int(entry_sticks.get())
	if (delete_sticks in [1, 2, 3]) and (sticks >= delete_sticks):
		sticks -= delete_sticks
		label_sticks.config(text=sticks*'|')
		status.config(text=sticks)
		counter += 1
		entry_sticks.delete(0, END)
		if counter % 2 == 0:
			label_move.config(text='Player 1, type a number from 1 to 3')
		else:
			label_move.config(text='Player 2, type a number from 1 to 3')
		if sticks == 1 and counter % 2 ==0:
			status.config(text='Player2 won!')
		if sticks == 1 and counter % 2 ==1:
			status.config(text='Player1 won!')
label_sticks = Label(text=sticks*'|', font='Arial 30 bold')
button = Button(text='Take sticks', font='Arial 15 bold', command=player)


label_move.pack()
entry_sticks.pack()
label_sticks.pack()
status.pack()
button.pack()
root.mainloop()
