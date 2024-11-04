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
currentRow = 3

Label(root, text='Part No.', width = 15, font=("Arial", 11)).grid(row = 1, column = 0, sticky = 'e', padx = 10, pady = 5)
Label(root, text='Serial No.', width = 15, font=("Arial", 11)).grid(row = 2, column = 0, sticky = 'e', padx = 10, pady = 5)
E1 = Entry(root, width = 30)
E2 = Entry(root, width = 30)
E1.grid(row = 1, column = 1, ipadx = 15, ipady = 5, sticky = 'w')
E2.grid(row = 2, column = 1, ipadx = 15, ipady = 5, sticky = 'w')

def addPart():
    global currentRow
    Label(root, text='Part No.', width = 15, font=("Arial", 11)).grid(row = currentRow, column = 0, sticky = 'e', padx = 10, pady = 5)
    currentRow += 1
    Label(root, text='Serial No.', width = 15, font=("Arial", 11)).grid(row = currentRow, column = 0, sticky = 'e', padx = 10, pady = 5)
    E1 = Entry(root, width = 30)
    E2 = Entry(root, width = 30)
    currentRow -= 1
    E1.grid(row = currentRow, column = 1, ipadx = 15, ipady = 5, sticky = 'w')
    currentRow += 1
    E2.grid(row = currentRow, column = 1, ipadx = 15, ipady = 5, sticky = 'w')
    currentRow += 1

    button1.grid(row = currentRow, column = 0, columnspan = 2, pady = 10)
    button2.grid(row = currentRow + 1, column = 0, columnspan = 2, pady = 10)

    root.grid_rowconfigure(0, weight = 1)
    root.grid_rowconfigure(currentRow + 2, weight = 1)

button1 = Button(root, text='Add Part', width=10, font=("Arial", 10), command = addPart)
button2 = Button(root, text='Go', width=5, font=("Arial", 10), command = root.destroy)

button1.grid(row = 3, column = 0, columnspan = 2, pady = 10)
button2.grid(row = 4, column = 0, columnspan = 2, pady = 10)

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(currentRow + 2, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_columnconfigure(2, weight = 1)

#scrollbar = Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)

#root.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=root.yview)

root.geometry("900x600")
root.mainloop()