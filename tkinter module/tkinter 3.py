from tkinter import*
top=Tk()
top.geometry("400x250")
name=Label(top,text="name").place(x=30,y=50)
email=Label(top,text="email").place(x=30,y=90)
passwad=Label(top,text="passward").place(x=30,y=130)

s1=Entry(top).place(x=90,y=50)
e2=Entry(top).place(x=90,y=90)
e3=Entry(top,show=90).place(x=90,y=130)
top.mainloop()
