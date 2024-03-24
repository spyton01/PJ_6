from tkinter import *
import tkinter  as tk

root = tk.Tk()
root.title("sign in")
root.geometry('300x200')


username=tk.StringVar()
passw=tk.StringVar()


#label description
name_label = tk.Label(root, text='Username')
name_entry = tk.Entry(root, textvariable=username)

passw_label = tk.Label(root, text='Password')
passw_entry = tk.Entry(root, textvariable=passw, show = '*')

#click bttn
sub_btn = tk.Button(root, text='Login')

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)

sub_btn.grid(row=2, columnspan=2)



root.mainloop()