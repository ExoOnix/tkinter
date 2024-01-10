from tkinter import *
from generator import *

gen = generator()
root = Tk()
root.geometry('300x200')
root.title('Password generator')
root.resizable(width=False, height=False)

labelframe1 = LabelFrame(text='Symbols')
check_lowercase = Checkbutton(labelframe1, text='abcdefghijklmnopqrstuvwxyz', command=generate_password)
check_numbers = Checkbutton(labelframe1, text='9123456789')
entry1 = Entry(labelframe1, width=15, state=DISABLED)
button_gen = Button(labelframe1, text='generate password', width=16, height=1)

labelframe1.pack(expand=True)
check_lowercase.pack(pady=3)
check_numbers.pack(pady=3)
entry1.pack(pady=3, anchor=CENTER)
button_gen.pack(pady=3, anchor=CENTER)
root.mainloop()