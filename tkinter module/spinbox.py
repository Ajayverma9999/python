from tkinter import*
top=Tk()

top.geometry("200x200")

spin=Spinbox(top,from_=1990,to=2022)
spin1=Spinbox(top,from_=1,to=31)

spin.pack(pady=10)
spin1.pack()

top.mainloop()
