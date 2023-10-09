from tkinter import*

top=Tk()
x=Menu(top)
file=Menu(x,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as....")
file.add_command(label="Close")

file.add_separator()

file.add_command(label="Exit",command=top.quit)

x.add_cascade(label="File",menu=file)
edit=Menu(x,tearoff=0)
edit.add_command(label="Undo")

edit.add_separator()

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

x.add_cascade(label="Edit",menu=edit)
help=Menu(x,tearoff=0)
help.add_command(label="About")
x.add_cascade(label="Help",menu=help)

top.config(menu=x)
top.mainloop()



