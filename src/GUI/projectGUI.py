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

Label(root, text='Part No.', width = 15, font=("Arial", 11)).grid(row = 1, column = 0, sticky = 'e', padx = 10, pady = 5)
Label(root, text='Serial No.', width = 15, font=("Arial", 11)).grid(row = 2, column = 0, sticky = 'e', padx = 10, pady = 5)
E1 = Entry(root, width = 30)
E2 = Entry(root, width = 30)
E1.grid(row = 1, column = 1, ipadx = 15, ipady = 5, sticky = 'w')
E2.grid(row = 2, column = 1, ipadx = 15, ipady = 5, sticky = 'w')

button1 = Button(root, text='Add Part', width=10, font=("Arial", 10))
button2 = Button(root, text='Go', width=5, font=("Arial", 10), command=root.destroy)

Label(root, text=' ').grid(row=0, column=1) 
Label(root, text=' ').grid(row=3, column=1) 
Label(root, text=' ').grid(row=5, column=1)

button1.grid(row = 4, column = 0, columnspan = 2, pady = 10)
button2.grid(row = 6, column = 0, columnspan = 2, pady = 10)

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(7, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_columnconfigure(2, weight = 1)

root.geometry("900x600")
root.mainloop()