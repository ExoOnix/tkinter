from tkinter import*
def add():
	todo = text.get() + '\n'
	list.insert(END, todo)
root = Tk()
root.resizable(width=False, height=False)
root.title("TODO list")
root.geometry('300x400')
btn = Button(text = "Save", command = add)
btn.pack()
text = Entry()
text.pack()
list = Text()
list.pack()
root.mainloop()