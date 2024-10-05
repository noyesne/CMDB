from tkinter import *

root = Tk()

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