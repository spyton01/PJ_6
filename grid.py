from tkinter import *
import tkinter  as tk

root = tk.Tk()
root.title("sign up")
root.geometry('350x200')


name=tk.StringVar()
email=tk.StringVar()
password=tk.StringVar()


#entry description display
name_label = tk.Label(root, text='Name', font=('Candara'))
name_entry = tk.Entry(root, textvariable=name, font=('Candara'))

email_label = tk.Label(root, text='Email',font=('Candara'))
email_entry = tk.Entry(root, textvariable=email, font=('Candara'))

password_label = tk.Label(root, text='Password',font=('Candara'))
password_entry = tk.Entry(root, textvariable=password, show = '*', font=('Candara'))

#click bttn
sub_btn = tk.Button(root, text='Sign up Now',font=('Candara'))

#adjust column
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)

password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)

sub_btn.grid(row=3, columnspan=2)



root.mainloop()