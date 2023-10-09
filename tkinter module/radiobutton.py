from tkinter import*

def selection():
    s="you selected the option"+str(radio.get())
    label.config(text=s)
top=Tk()
top.geometry("300x150")
radio=IntVar()
lbl=Label(top,text="you gender:")
lbl.pack()
R1=Radiobutton(top,text="Male",variable=radio,value=1,
               command=selection)
R1.pack()

R2=Radiobutton(top,text="Female",variable=radio,value=2,
               command=selection)
R2.pack()

label=Label(top)
label.pack()
top.mainloop()
