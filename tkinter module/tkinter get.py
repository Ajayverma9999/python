from tkinter import*
def show_entry_fields():
    a=e1.get()
    b=e2.get()
    l1.configure(text=a)
    l2.configure(text=b)

master=Tk()
Label(master,text="first name").grid(row=0,column=0)
Label(master,text="last name").grid(row=1,column=0)

e1=Entry(master)
e2=Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(master,text='Quit',command=master.quit).grid(row=3,column=0)
Button(master,text='show',command=show_entry_fields).grid(row=3,column=1)

l1=Label(master)
l1.place(x=50,y=80)
l2=Label(master)
l2.place(x=100,y=80)
master.mainloop()
