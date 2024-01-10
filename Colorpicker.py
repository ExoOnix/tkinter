from tkinter import *
import pyperclip
root = Tk()
root.geometry('550x300')
root.resizable(False, False)
root.title('Color picker')

def color_generate(value):
	red = R.get()
	green = G.get()
	blue = B.get()
	color = f'#{red:02x}{green:02x}{blue:02x}'
	label_color.config(bg=color, text=color)
	if color == '#ffffff':
		label_color.config(fg='Black')
	else:
		label_color.config(fg='White')
	pyperclip.copy(color)
	spam = pyperclip.paste()
frame_RGB = LabelFrame(text='Choose color', height=250, width=250)
frame_color = LabelFrame(text='Color', height=250, width=250)
label_color = Label(frame_color, text='Color picker', font='arial 15 bold', height=8, width=16, fg='white', bg='black')

R = Scale(frame_RGB, label='Red', fg='Red', to=255, length=200, orient=VERTICAL, command=color_generate)
G = Scale(frame_RGB, label='Green', fg='Green', to=255, length=200, orient=VERTICAL, command=color_generate)
B = Scale(frame_RGB, label='Blue', fg='Blue', to=255, length=200, orient=VERTICAL, command=color_generate)

R.place(x=1, y=1)
G.place(x=80, y=1)
B.place(x=160, y=1)

frame_RGB.place(x=5, y=10)
frame_color.place(x=295, y=10)
label_color.place(x=25, y=10)

root.mainloop()