import tkinter as tk
from tkinter import ttk
import oracledb as db

home=tk.Tk()
home.geometry('500x500')
home.title('HOME')


f_home = tk.Frame(home)

home_li={"ID":0,"PW":1}

for text, num in home_li.items():
    label=tk.Label(f_home,text=text, font=("Arial",15),pady=5)
    label.grid(row=num,column=0)
    entry=tk.Entry(f_home,font=("Arial",15))
    entry.grid(row=num,column=1)

f_home.pack(pady=50)

home.mainloop()