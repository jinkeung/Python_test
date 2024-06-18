import tkinter as tk
from tkinter import ttk
import oracledb as db

root=tk.Tk()
root.geometry('1000x500')

#Treeview: 2차원 배열을 표현하기 위한 개체

frame=tk.Frame(root)
tree=ttk.Treeview(frame,columns=("sub","num"))
tree.column("sub")
tree.heading("#0",text="TITLE")
tree.heading("sub",text="SUB")
tree.heading("num",text="NUM")

con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
cursor=con.cursor()
cursor.execute('select * from title')
for i in cursor.fetchall():
    title=tree.insert("","end",text=i[0])
    t_num=i[1]
    for j in cursor.execute('select sub,num from %s' %t_num):
        tree.insert(title,"end",values=[j[0],j[1]])
cursor.close()
con.close()

scroll=ttk.Scrollbar(frame,orient=tk.VERTICAL,command=tree.yview)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
scroll2=ttk.Scrollbar(frame,orient=tk.HORIZONTAL,command=tree.xview)
scroll2.pack(side=tk.BOTTOM,fill=tk.X)
tree.config(yscrollcommand=scroll.set,      #treeview가 이미 배치되어있는 상태라
            xscrollcommand=scroll2.set)     #scroll 넣고 treeview 변경해줘야적용됨

tree.pack()
frame.pack()

def data():
    li.delete(0,tk.END)
    title=tree.item(tree.selection(),"text")
    con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
    cursor=con.cursor()
    cursor.execute('select t_num from title where title=:title',title=title)
    t_num=cursor.fetchone()[0]
    cursor.execute('select sub from %s' %t_num)
    for i in cursor.fetchall():
        li.insert("end",i[0])




button=tk.Button(root,text="Click Me!",command=data)
button.pack()

li=tk.Listbox(root)
li.pack(pady=10)
root.mainloop()