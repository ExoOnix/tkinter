import zodiac
from tkinter import *



root = Tk()
root.geometry('300x500')
root.title('Zodiac')
root.resizable(width=False, height=False)
index = 0


def click():
	global index, entry1, entry2, zodiac_names, zodiac_files, name
	d = int(entry1.get())
	m = int(entry2.get())
	index = zodiac.define(d, m)
	nzodiac = zodiac_names[index]
	fzodiac = zodiac_files[index]
	name.config(text=nzodiac)
	gif.config(file=fzodiac)
	image.config(image=gif)
gif = PhotoImage(file='img/start.gif')
zodiac_names = ['Incorrect date', 'Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gimini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagattarius']
zodiac_files = ['img/start.gif', 'img/capricorn.gif', 'img/aquarius.gif', 'img/pisces.gif', 'img/aries.gif', 'img/taurus.gif', 'img/gemini.gif', 'img/cancer.gif', 'img/leo.gif', 'img/virgo.gif', 'img/libra.gif', 'img/scorpio.gif', 'img/sagittarius.gif']

enterlabel = LabelFrame(text='Date of birthdate', width=290, height=120)
label1 = Label(enterlabel, text='Enter day', font='Arial 13')
entry1 = Entry(enterlabel, width=30)

label2 = Label(enterlabel, text='Enter month', font='Arial 13')
entry2 = Entry(enterlabel, width=30)

button = Button(enterlabel, text='Check zodiac', width=13, height=1, command=click)
name = Label(text='Enter your birthdate', font='Arial 16')
image = Label(image=gif)


enterlabel.pack()
label1.grid(row=0, column=0, sticky=W, pady=8)
entry1.grid(row=0, column=1, padx=8)

label2.grid(row=1, column=0, sticky=W, pady=8)
entry2.grid(row=1, column=1, padx=8)

button.grid(row=2, column=0, columnspan=2)
name.pack()
image.pack(expand=True)

root.mainloop()
