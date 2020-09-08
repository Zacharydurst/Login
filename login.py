# Imports
import tkinter as tk
from tkinter import messagebox
import pyodbc
import os
import hashlib

# Wrapper function and size of window.
login = tk.Tk()
login.geometry("300x200")

# Name text and entry field.
name = tk.Label(text = 'Enter username')
name.pack()
entry_name = tk.Entry()
entry_name.pack()

# Password text and entry field.
password = tk.Label(text = 'Enter password')
password.pack()
entry_password = tk.Entry(show = '*')
entry_password.pack()

# Function to check if username and password exist already in DB.
def login_attempt():
    user_name = entry_name.get()
    pass_word = entry_password.get()
    sql = ("SELECT * FROM Mydb.dbo.user_info where username = ?")
    mycursor.execute(sql, user_name)
    for info in mycursor.fetchall():
        found = False
        old_salt = info[2]
        new_key = hashlib.pbkdf2_hmac('sha256', pass_word.encode('utf-8'), old_salt, 100000)
        if info[0] == user_name and info[1] == new_key:
            print("success")
            found = True
            entry_name.delete(0, "end")
            entry_password.delete(0, "end")
            tk.messagebox.showinfo(title = 'Alert', message = 'Logged in!')
            close_window()
        if found == False:
            tk.messagebox.showinfo(title = 'Alert', message = 'Incorrect Login. Please Try Again.')
            entry_name.delete(0, "end")
            entry_password.delete(0, "end")

    # Loop to check if user exists in SQL DB
    for users in mycursor.fetchall():
        print(users)
        
    



# Function that runs register.py for users to create a username and password.
def start_registration():
    os.system('python register.py')

def close_window():
    login.destroy()

# Creation of login button.
login_button = tk.Button(login, text = 'Click here to login.', command = login_attempt)
login_button.pack()

# Creation of registration button.
registration_button = tk.Button(login, text = 'Need to register? Click here!', command = start_registration)
registration_button.pack()

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
    login.mainloop()

if __name__ == "__main__":
    main()



