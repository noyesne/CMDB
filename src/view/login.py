import tkinter as tk
from tkinter import messagebox
import projectGUI


flag = False
# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    # You can add your own validation logic here
    if userid == "admin" and password == "password":
        parent.quit()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

# Set the window size (width x height)
parent.geometry("400x250")  # Adjust the size as needed

# Configure the grid to have weights so widgets can be centered
parent.grid_rowconfigure(0, weight=1)  # Center vertically
parent.grid_rowconfigure(4, weight=1)  # Center vertically
parent.grid_columnconfigure(0, weight=1)  # Space on the left
parent.grid_columnconfigure(3, weight=1)  # Space on the right

# Create and place the username label and entry
username_label = tk.Label(parent, text="User ID:")
username_label.grid(row=1, column=1, sticky="e", padx=10, pady=10)  # Align to right

username_entry = tk.Entry(parent)
username_entry.grid(row=1, column=2, padx=10, pady=10)  # Entry box centered

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.grid(row=2, column=1, sticky="e", padx=10, pady=10)  # Align to right

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.grid(row=2, column=2, padx=10, pady=10)  # Entry box centered

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.grid(row=3, column=1, columnspan=2, pady=20)  # Center the button across columns

projectGUI.main()
# Start the Tkinter event loop
parent.mainloop()

