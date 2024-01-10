from tkinter import *
from random import *
root = Tk()
root.geometry('200x260')

def generate_alarms():
    alarmbox.delete(0, END)
    alarms = []
    a = 0
    b = 5
    for i in range(10):
        randomtime = randint(a, b)
        # <Решение проблемы-1>
        if len(str(randomtime)) == 1:
           alarms.append(f'07:0{randomtime}')
        else:
           alarms.append(f'07:{randomtime}')
        # </Решение проблемы-1>
        a, b = b + 1, b + 6
    alarmbox.insert(END, *alarms)
def delete_alarms():
	alarmbox.delete(ACTIVE)

def open_change_window():
    global newalarm, change_window
    change_window = Toplevel()
    label2 = Label(change_window, text='Enter the time', font='Arial 10', justify=CENTER)
    newalarm = Entry(change_window, text='hi', width=15, justify=CENTER)
    save_button = Button(change_window, text='Save', height=1, width=15, justify=CENTER, command=change_alarm)
    label2.pack()
    newalarm.pack()
    save_button.pack()


def change_alarm():
    alarmbox.delete(ACTIVE)
    alarmbox.insert(ACTIVE, newalarm.get())
    change_window.destroy()


label1 = Label(text='Alarm', font='Arial 10', justify=CENTER)
status = Label(text='', font='Arial 10', justify=CENTER)
alarmbox = Listbox(width=30, height=10, justify=CENTER, selectmode=SINGLE)
btn1 = Button(text='Random alarms', height=1, width=15, justify=CENTER, command=generate_alarms)
btn2 = Button(text='Delete alarms', height=1, width=15, justify=CENTER, command=delete_alarms)
btn3 = Button(text='Edit alarms', height=1, width=15, justify=CENTER, command=open_change_window)



label1.pack()
alarmbox.pack()
btn1.pack()
btn2.pack()
btn3.pack()
root.mainloop()