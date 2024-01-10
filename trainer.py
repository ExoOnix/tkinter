from tkinter import*
from random import randint
root = Tk()
root.geometry('460x300')
numF = randint(1, 999) / 10
numF01 = numF
def cancelOper():
	global numF
	global numF01
	numF = numF01
	num.config(text=str(numF))
def intDivBy10():
	global numF
	numF //= 10
	num.config(text=str(numF))
def modOper10():
	global numF
	numF %= 10
	num.config(text=str(numF))
def divBy10():
	global numF
	numF /= 10
	num.config(text=str(numF))
def mulBy10():
	global numF
	numF *= 10
	num.config(text=str(numF))
def intDivBy1():
	global numF
	numF//= 1
	num.config(text=str(numF))
def modOper1():
	global numF
	numF %= 1
	num.config(text=str(numF))
def divBy1():
	global numF
	numF /= 1
	num.config(text=str(numF))
def mulBy1():
	global numF
	numF *= 1
	num.config(text=str(numF))
num = Label(root, text = str(numF), font='Verdana 48')
btn10_1 = Button(root, text='// 10', width=7, font='Verdana 18', command=intDivBy10)
btn10_2 = Button(root, text='% 10', width=7, font='Verdana 18', command=modOper10)
btn10_3 = Button(root, text='/ 10', width=7, font='Verdana 18', command=divBy10)
btn10_4 = Button(root, text='* 10', width=7, font='Verdana 18', command=mulBy10)
btn1_1 = Button(root, text='// 1', width=7, font='Verdana 18', command=intDivBy1)
btn1_2 = Button(root, text='% 1', width=7, font='Verdana 18', command=modOper1)
btn1_3 = Button(root, text='/ 1', width=7, font='Verdana 18', command=divBy1)
btn1_4 = Button(root, text='* 1', width=7, font='Verdana 18', command=mulBy1)
btn_cancel = Button(root, text='Cancel', font='Verdana 18', command=cancelOper)
num.grid(row=0, column=0, columnspan=4)
btn10_1.grid(row=1, column=0)
btn10_2.grid(row=1, column=1)
btn10_3.grid(row=1, column=2)
btn10_4.grid(row=1, column=3)
btn1_1.grid(row=2, column=0)
btn1_2.grid(row=2, column=1)
btn1_3.grid(row=2, column=2)
btn1_4.grid(row=2, column=3)
btn_cancel.grid(row=3, column=1, columnspan=2)
root.mainloop()
