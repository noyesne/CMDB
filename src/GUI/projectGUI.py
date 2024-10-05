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

Label(root, text='Part No.', width = 10).grid(row = 1)
Label(root, text='Serial No.', width = 10).grid(row = 2)
E1 = Entry(root, width = 30)
E2 = Entry(root, width = 30)
E1.grid(row = 1, column = 1)
E2.grid(row = 2, column = 1)

button1 = Button(root, text='Add Part', width=10)
button2 = Button(root, text='Go', width=5, command=root.destroy)

blank = Label(root, text=' ')
blank2 = Label(root, text=' ')
blank3 = Label(root, text=' ')
blank.grid(row = 0, column = 1)
blank2.grid(row = 3, column = 1)
blank3.grid(row = 5, column = 1)

button1.grid(row = 4, column = 0, columnspan = 2)
button2.grid(row = 6, column = 0, columnspan = 2)

root.geometry("270x180")
root.mainloop()