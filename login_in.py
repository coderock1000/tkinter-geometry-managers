import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

root = tk.Tk()
root.title("Login Screen")
root.geometry("300x200")
root.configure(bg='gray')

tk.Label(root, text="Username:", bg='gray').pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:", bg='gray').pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack(pady=20)

root.mainloop()
