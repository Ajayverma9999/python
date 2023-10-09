from tkinter import*
master=Tk()
def var_states():
    print("Cricket:",var1.get())
    print("Football:",var2.get())


Label(master,text="hobbies:").grid(row=0,column=0)
var1=IntVar()

Checkbutton(master,text="Cricket:",variable=var1).grid(row=1,column=0)
var2=IntVar()


Checkbutton(master,text="Football:",variable=var2).grid(row=2,column=0)
Button(master,text='Quit:',command=master.quit).grid(row=3,column=0)
Button(master,text='show:',command=var_states).grid(row=4,column=0)
master.mainloop()
