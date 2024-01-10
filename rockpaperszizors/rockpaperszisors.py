from tkinter import *
import random as rdm

class Main(Frame):
	def __init__(self, root):
		super(Main, self).__init__(root)
		self.startUI()
	def btn_click(self, choise):
		comp_choise = rdm.randint(1, 3)
		if choise == comp_choise:
			self.drow += 1
			self.lbl.config(text='Draw')
		elif (choise == 1 and comp_choise ==2) or (choise == 2 and comp_choise == 3) or (choise == 3 and comp_choise == 1):
			self.win += 1
			self.lbl.config(text='You won')
		else:

			self.lose += 1
			self.lbl.config(text='You lost')
		self.lbl2.config(text=f'Wins: {self.win}\nDraws: {self.drow}\nLoses: {self.lose}')

		del comp_choise


	def startUI(self):
		self.win = self.drow = self.lose = 0
		btn = Button(root, text='rock', font=('Times New Roman', 15), command=lambda x=1:self.btn_click(x))
		btn2 = Button(root, text='scisors', font=('Times New Roman', 15), command=lambda x=2: self.btn_click(x))
		btn3 = Button(root, text='paper', font=('Times New Roman', 15), command=lambda x=3: self.btn_click(x))

		self.lbl = Label(root, text='starting!', bg='#FFF', font=('Times New Roman', 21, 'bold'))
		self.lbl.place(x=120, y=25)

		self.lbl2 = Label(root, justify='left', font=('Times New Roman', 21, 'bold'), text=f'Wins: {self.win}\nDraws: {self.drow}\nLoses: {self.lose}', bg='#FFF')
		self.lbl2.place(x=5, y=5)


		btn.place(x=10, y=100, width=120, height=50)
		btn2.place(x=155, y=100, width=120, height=50)
		btn3.place(x=300, y=100, width=120, height=50)
		pass
if __name__ == '__main__':
	root = Tk()
	root.geometry('500x500+200+200')
	root.title('Rock paper scisors')
	root.resizable(width=False, height=False)
	root['bg'] == '#FFF'
	app = Main(root)
	app.pack()
	root.mainloop()