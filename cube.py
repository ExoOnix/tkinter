from tkinter import *
from random import randint

def roll():
	text.delete(0.0, END)
	text.insert(END, str(randint(1,6)))
root = Tk()
text = Text(root, width=5, height=2)
buttonA = Button(root, text='Roll', command=roll)
text.pack()
buttonA.pack(pady=5)
root.mainloop()