from tkinter import *
import tkinter  as tk

root = tk.Tk()
root.title("sign in")
root.geometry('300x200')


username=tk.StringVar()
password=tk.StringVar()


#label description display
name_label = tk.Label(root, text='Username')
name_entry = tk.Entry(root, textvariable=username)

password_label = tk.Label(root, text='Password')
password_entry = tk.Entry(root, textvariable=password, show = '*')

sub_btn = tk.Button(root, text='Login')

#geometry
name_label.place(x=30, y=50)
name_entry.place(x=120, y=50)

password_label.place(x=30, y=80)
password_entry.place(x=120, y=80)

sub_btn.place(x=130, y=120)



root.mainloop()