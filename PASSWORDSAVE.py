from tkinter import*
root = Tk()
root.geometry('400x300')
root.title('PASSWORD')

def showpass():
	password = inputbox.get()
	if 6 > len(password):
		label2.config(text = 'Password too small', fg = 'red')
	else:
		label2.config(text = password, fg = 'blue')
def blackbac():
	root.config(bg = '#353535')
	passwordbox.config(bg = '#353535', fg = 'white')
	label1.config(bg = '#353535', fg = 'white')
	label2.config(bg = '#353535')
	showbutton.config(bg = '#535353', fg = 'white')
	blackbac_btn.config(bg = '#535353', fg = 'white', state = DISABLED)


passwordbox = LabelFrame(text = 'Password')
label1 = Label(passwordbox, text = 'Enter passsword', font = 'Arial 10')
label2 = Label(passwordbox, text = '', font = 'Arial 10')
showbutton = Button(passwordbox, text = 'Show', height = 1, width = 15, command = showpass)
inputbox = Entry(passwordbox, bg = 'black', fg = 'white', font = 'Arial 12', justify = CENTER, relief = RAISED, width = 10, state = NORMAL, show = "*")
blackbac_btn = Button(passwordbox, text = 'Dark mode', height = 1, width = 15, command = blackbac)

passwordbox.pack(expand = True)
label1.pack()
inputbox.pack()
label2.pack()
showbutton.pack()
blackbac_btn.pack()

root.mainloop()