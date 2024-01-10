from tkinter import *
import random
from tkinter import messagebox
import time
root = Tk()
root.geometry('550x300')
root.title('Schulte')
root.resizable(width=False, height=False)


def restart():
	global numbers_in_order, game_frame, start_time, greeting_frame
	MsgBox = messagebox.askquestion ('Begin the game','The timer will start if you click yes.',icon = 'warning')
	if MsgBox == 'yes':
		greeting_frame.forget()
		numbers_in_order = [x for x in range(1, 10)]
		random_numbers = [x for x in range(1, 10)]
		random.shuffle(random_numbers)
		game_frame = Frame()
		game_frame.pack(expand=True)
		start_time = time.time()

		row = 0
		column = 0

		for n in random_numbers:
			button = Button(game_frame, text=n, font='Arial 15 bold', width=8, height=3)
			button.grid(row=row, column=column)
			button.bind('<Button-1>', click)
			column += 1
			if column == 3:
				row += 1
				column = 0
	else:
		game_frame.destroy()
		greeting_frame.pack(expand=True)


def click(event):
	global numbers_in_order, game_frame, greeting_frame, start_time
	if event.widget['text'] == numbers_in_order[0]:
		numbers_in_order.pop(0)
		event.widget.unbind('<Button-1')
		event.widget['state'] = 'disabled'
		event.widget['bg'] = 'green'
		if len(numbers_in_order) == 0:
			end_time = time.time()
			messagebox.showinfo('Congrats!', f'You have won.\n Your time is: {round(end_time-start_time, 3)}.')
			game_frame.destroy()
			greeting_frame.pack(expand=True)
	else:
		messagebox.showerror('You loose!', 'You made a mistake. Try again.')
		game_frame.destroy()
		restart()



def start(event):
	global game_frame, greeting_frame
	MsgBox1 = messagebox.askquestion ('Are you sure?', 'Are you sure you want to return to the menu?',icon = 'warning')
	if MsgBox1 == 'yes':
		game_frame.destroy()
		greeting_frame.pack(expand=True)


greeting_frame = Frame()
labeltitle = Label(greeting_frame, text='Schulte', font='Arial 18 bold')
label = Label(greeting_frame, text='Schulte is a game that improves\nyour eyes, reading speed and reaction!\n Game rules:\n 1. Player should faster then everyone select the buttons from 1 - 9 \n2. If the player fails - he has to begin again. \n3. The player who wins is the one who fineshed this game the fastest.', font='Arial 10', justify=LEFT)
button = Button(greeting_frame, text='Start game', width=10, height=2, justify=CENTER, command=restart)

greeting_frame.pack(expand=True)
labeltitle.pack()
label.pack()
button.pack(pady=20)
root.bind('<Escape>', start)
root.mainloop()
