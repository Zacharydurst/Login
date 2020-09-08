# Imports
import tkinter as tk
from tkinter import messagebox
import pyodbc
import hashlib
import os

# Wrapper function and size of window.
register = tk.Tk()
register.geometry('300x200')

# Name text and entry field.
name = tk.Label(text = 'Enter in a username to register:')
name.pack()
entry_name = tk.Entry()
entry_name.pack()

# Password text and entry field.
password = tk.Label(text = 'Enter in a password')
password.pack()
entry_password = tk.Entry(show = "*")
entry_password.pack()

# Confirm password text and entry field.
confirm_password = tk.Label(text = 'Confirm your password')
confirm_password.pack()
entry_confirm_password = tk.Entry(show = '*')
entry_confirm_password.pack()

# Function to close window after registration is complete.
def close_registration_window():
    register.destroy()

# Function to insert username and password into DB.
def insert_into_sql():
    user_name = entry_name.get()
    password = entry_password.get()
    password_2 = entry_confirm_password.get()
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    if password == password_2:
        sql = ("INSERT INTO Mydb.dbo.user_info (username, hash, salt) VALUES (?, ?, ?)")
        mycursor.execute(sql, user_name, key, salt)
        mydb.commit()
        entry_name.delete(0, "end")
        entry_password.delete(0 ,"end")
        entry_confirm_password.delete(0, "end")
        tk.messagebox.showinfo(title = 'Alert', message = 'User registered!')
        close_registration_window()
    else:
        tk.messagebox.showinfo(title = 'Alert', message = 'Passwords do not match!')
    
# Register user/submit button.
register_button = tk.Button(register, text = 'Register User', command = insert_into_sql)
register_button.pack()


# Main function to kick off script.
def main():
    # Connection to SQL DB.
    mydb = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=XPTA500272-P50;'
    'Database=Mydb;'
    'Trust_Connection=yes;')

    # Creation of cursor for SQL DB session.
    mycursor = mydb.cursor()

    # Infinite loop for the window to display.
    register.mainloop()

if __name__ == "__main__":
    main()
