from tkinter import *
root = Tk()
root.geometry('250x300')
root.title('Calculator')



labelframe1 = LabelFrame(text='Enter the values', height=100, width=50)
labelframe2 = LabelFrame(text='Anser', height=100, width=250)
entry_a = Entry(labelframe1, width=3)
entry_b = Entry(labelframe1, width=3)
entry_c = Entry(labelframe1, width=3)
label1 = Label(labelframe1, text='x**2 +', font='Arial 11')
label2 = Label(labelframe1, text='x +', font='Arial 11')
label3 = Label(labelframe1, text='= 0', font='Arial 11')
output = Text(labelframe2, width=30, height=10)
button = Button(text='Calculate', height=1, width=10)

labelframe1.grid(column=0, row=0, columnspan=3)
labelframe2.grid(column=0, row=1, columnspan=3, pady=15)


entry_a.grid(column=1, row=0, padx=7)
entry_b.grid(column=3, row=0, padx=7)
entry_c.grid(column=5, row=0, padx=7)
label1.grid(column=2, row=0, padx=7)
label2.grid(column=4, row=0, padx=7)
label3.grid(column=6, row=0, padx=7)
output.grid(column=0, row=0, columnspan=3)
button.grid(column=0, row=2, columnspan=3)
root.mainloop()