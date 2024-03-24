from tkinter import *
import tkinter  as tk

root = tk.Tk()
root.title("sign up")
root.geometry('300x200')


name=tk.StringVar()
email=tk.StringVar()
password=tk.StringVar()


#entry description display
name_label = tk.Label(root, text='Name')
name_entry = tk.Entry(root, textvariable=name)

email_label = tk.Label(root, text='Email')
email_entry = tk.Entry(root, textvariable=email)

password_label = tk.Label(root, text='Password')
password_entry = tk.Entry(root, textvariable=password, show = '*')

#click bttn
sub_btn = tk.Button(root, text='Sign up Now')

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)

password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)

sub_btn.grid(row=3, columnspan=2)



root.mainloop()