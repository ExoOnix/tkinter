from tkinter import*


root = Tk()
root.title("Chemistry")
root.geometry('220x500')
elements=['O', 'H','C', 'S', 'Cl', 'Na']
sub1=['OH', 'OC', 'OHS', 'HCI', 'ClNa', 'OHNa', 'HS', 'OS', 'OSNa', 'HC', 'CNa', 'OCl']
sub2=['H2O', 'CO2', 'H2SO4', 'HCI', 'NaCl', 'NaOH', 'H2S', 'SO2', 'Na2SO4', 'CH4', 'Na3C', 'Cl207']
sub3=['water', 'carbon dioxide', ' sulfuric acid', ' hydrochloric acid', 'table salt', 'caustic soda',  'hydrogen sulfide' , 'sulfur oxide', 'sodium sulfate', 'methane ', 'sodium carbide', 'chlorine oxide']

root.resizable(width=False, height=False)

image = PhotoImage(file='flask1.gif')

elem1 = BooleanVar()
elem1.set(0)
el1 = Checkbutton(text="O", variable=elem1, onvalue=1, offvalue=0, indicatoron=0, font='Arial 20', width=4, height=1)

elem2 = BooleanVar()
elem2.set(0)
el2 = Checkbutton(text="H", variable=elem2, onvalue=1, offvalue=0, indicatoron=0, font='Arial 20', width=4, height=1)

elem3 = BooleanVar()
elem3.set(0)
el3 = Checkbutton(text="C", variable=elem3, onvalue=1, offvalue=0, indicatoron=0, font='Arial 20', width=4, height=1)

elem4 = BooleanVar()
elem4.set(0)
el4 = Checkbutton(text="S", variable=elem4, onvalue=1, offvalue=0, indicatoron=0, font='Arial 20', width=4, height=1)

elem5 = BooleanVar()
elem5.set(0)
el5 = Checkbutton(text="Cl", variable=elem5, onvalue=1, offvalue=0, indicatoron=0, font='Arial 20', width=4, height=1)

elem6 = BooleanVar()
elem6.set(0)
el6 = Checkbutton(text="Na", variable=elem6, onvalue=1, offvalue=0, indicatoron=0, font='Arial 20', width=4, height=1)

def mix():
	substance=""
	btncheck=[elem1.get(), elem2.get(), elem3.get(), elem4.get(), elem5.get(), elem6.get()]
	for i in range (len(btncheck)):
		if btncheck[i]==1:
			substance=substance+elements[i]
	if sub1.count(substance)!=0:
		a=sub1.index(substance)
		lb_2.config(text=sub2[a])
		lb_3.config(text=sub3[a])
	else:
		lb_2.config(text="")
		lb_3.config(text="did not find connection")

btn=Button(text="Mix elements", bg='#87CEEB', width=20, height=2, font='Arial 10', command=mix)



lb_1=Label(text='Chemicals', font='Arial 14', fg='blue', bg='#ffffff', width=20, height=2)
lb_2=Label(text="", image=image, font='Arial 14', fg='black', bg='#ffffff', width=220, height=280, compound=CENTER)
lb_3=Label(text="", font='Arial 14', fg='black', bg='#ffffff', width=20, height=1)


lb_1.grid(row=0,column=0,columnspan=3)
lb_2.grid(row=4,column=0,columnspan=3)
lb_3.grid(row=5,column=0,columnspan=3)
el1.grid(row=1, column=0)
el2.grid(row=1, column=1)
el3.grid(row=1, column=2)
el4.grid(row=2, column=0)
el5.grid(row=2, column=1)
el6.grid(row=2, column=2)
btn.grid(row=3, column=0, columnspan=3)
root.mainloop()