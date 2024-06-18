import tkinter as tk
import work0610_1_bs as bs

home=tk.Tk()
home.geometry('1000x1000')

f_home=tk.Frame(home)
li_title=tk.Listbox(f_home,width=100)
for i in bs.news_title():
    li_title.insert(tk.END, i)
li_title.pack()
f_home.pack()
home.mainloop()