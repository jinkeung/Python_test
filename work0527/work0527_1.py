import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mbox

#tk
#Label, Button, Entry, Listabox, Treeview, ratioButton, Canvas ...

def click():
    mbox.showinfo("Info",entry.get())

def li_print():
    print(list.get(list.curselection()))        #커서로 선택한 대상의 값 get


home=tk.Tk()
home.title("HOME")
home.geometry("500x500")



label=tk.Label(home, text="Hello World", font=("Helvetica", 20))
label.pack()
button=tk.Button(home, text="Click Me",font=("Helvetica", 15),command=click)
button.pack(pady=10)
entry=tk.Entry(home, font=("Helvetica", 15))
entry.pack(pady=10)
list=tk.Listbox(home, font=("Helvetica", 15))
list.insert("end","Hello")
list.insert(tk.END,"World")
list.insert("end","Robot")
list.insert("end","HI")
list.pack(pady=10,fill="x")
button2=tk.Button(home, text="print",font=("Helvetica", 15),command=li_print)
button2.pack(pady=10)


home.mainloop()