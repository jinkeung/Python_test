import tkinter as tk
import oracledb as db

def title():
    con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
    cursor=con.cursor()
    cursor.execute("select title from title")
    for i in cursor.fetchall():
        li_left.insert("end",i[0])
    cursor.close()
    con.close()

def click(e):
    li_right.delete(0,tk.END)
    title=li_left.get(li_left.curselection())
    con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
    cursor=con.cursor()
    cursor.execute("select t_num from title where title=:title",title=title)
    t_num=cursor.fetchone()[0]
    cursor.execute("select sub from %s" %t_num)
    for i in cursor.fetchall():
        li_right.insert("end",i[0])

window=tk.Tk()
window.geometry('700x700')
window.title('WINDOW')

frame=tk.Frame(window)
li_left=tk.Listbox(frame,width=30,height=30,font=("Arial",12))
li_left.grid(row=0, column=0)
title()
li_left.bind("<ButtonRelease>",click)

li_right=tk.Listbox(frame,width=30,height=30,font=("Arial",12))
li_right.grid(row=0, column=1)


frame.pack(pady=20)


window.mainloop()