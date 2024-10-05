from tkinter import *

root = Tk()
# create a menu at the top of the screen
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Input')
filemenu.add_command(label='Output')
filemenu.add_command(label='Save Config')
filemenu.add_command(label='Load Config')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
editmenu = Menu(menu)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Add Component')

# this creates a label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Luca Martinez")

# shoves it onto the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

button1 = Button(root, text='Start', width=25)
button2 = Button(root, text='Stop', width=25, command=root.destroy)

button1.grid(row = 0, column = 1)
button2.grid(row = 1, column = 1)

root.mainloop()