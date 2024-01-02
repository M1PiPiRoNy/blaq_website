import tkinter as tk
from tkinter import messagebox
import os 

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login Page")

        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)

        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")

        self.login_button = tk.Button(self, text="Login", command=self.authenticate)

        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=10)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.login_button.pack(pady=20)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check the hardcoded username and password
        if username == "user1" and password == "pass1":
            self.destroy()
            Page1(username)
        elif username == "user2" and password == "pass2":
            self.destroy()
            Page2(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class Page1(tk.Tk):


    os.system('python3 main.py')
    def __init__(self, username):
        super().__init__()

        self.title("Page 1")
        label = tk.Label(self, text=f"Welcome, {username}, to Page 1")
        label.pack(pady=20)
    
        self.mainloop()
        

class Page2(tk.Tk):
    def __init__(self, username):
        super().__init__()

        self.title("Page 2")
        label = tk.Label(self, text=f"Welcome, {username}, to Page 2")
        label.pack(pady=20)

        self.mainloop()

if __name__ == "__main__":
    login_page = LoginPage()
    login_page.mainloop()
