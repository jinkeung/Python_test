"""
엔트리 4개에 값 입력
=>1번버튼 : DB에 추가
입력된 데이터를 오라클 DB를 통해 필드 단위로 하나씩 저장
=>2번 버튼클릭=> treeview와 tkagg 새로운 창, 데이터베이스 적재된 모든 row tuple, record
"""

import tkinter as tk
import oracledb as db
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.messagebox as mbox
def add():
    con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
    cursor=con.cursor()
    try:
        cursor.execute('insert into entry(e1,e2,e3,e4) values(:e1,:e2,:e3,:e4)',
                       e1=int(e1.get()),e2=int(e2.get()),e3=int(e3.get()),e4=int(e4.get()))
        con.commit()
        cursor.close()
        con.close()
        e1.delete(0,tk.END)
        e2.delete(0,tk.END)
        e3.delete(0,tk.END)
        e4.delete(0,tk.END)
    except Exception:
        mbox.showerror("ERROR","4칸 전부 숫자 입력")
        pass

def data():
    data=tk.Toplevel()
    data.geometry('1200x700')

    f_tree=tk.Frame(data)
    tv=ttk.Treeview(f_tree,columns=('e1','e2','e3','e4'))
    tv.column('e1',anchor="e",width=100)
    tv.column('e2',anchor="e",width=100)
    tv.column('e3',anchor="e",width=100)
    tv.column('e4',anchor="e",width=100)
    tv.heading("#0",text="num")
    tv.heading("e1",text="entry1")
    tv.heading("e2",text="entry2")
    tv.heading("e3",text="entry3")
    tv.heading("e4",text="entry4")
    con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
    cursor=con.cursor()
    cursor.execute('select * from entry order by s_num asc')
    for i in cursor.fetchall():
        tv.insert("","end",text=i[0],values=[i[1],i[2],i[3],i[4]])


    scroll=ttk.Scrollbar(f_tree,orient=tk.VERTICAL,command=tv.yview)
    scroll.pack(side=tk.RIGHT,fill=tk.Y)
    tv.config(yscrollcommand=scroll.set)
    tv.pack()
    f_tree.pack(pady=10)

    f_graph=tk.Frame(data)
    cursor.execute('select e1,e2,e3,e4 from entry')
    arr=list()
    for i in cursor.fetchall():
        for j in i:
            arr.append(j)

    fig,ax=plt.subplots(nrows=1,ncols=1,figsize=(5,10))
    ax.hist(arr,bins=10)
    canvas=FigureCanvasTkAgg(fig, f_graph)
    canvas.get_tk_widget().pack()
    f_graph.pack(pady=10)
    data.mainloop()

window=tk.Tk()
window.geometry('500x700')
frame=tk.Frame(window)
e1=tk.Entry(frame,width=20,font=("Arial",15))
e1.pack(pady=10)
e2=tk.Entry(frame,width=20,font=("Arial",15))
e2.pack(pady=10)
e3=tk.Entry(frame,width=20,font=("Arial",15))
e3.pack(pady=10)
e4=tk.Entry(frame,width=20,font=("Arial",15))
e4.pack(pady=10)
frame.pack(pady=100)

frame2=tk.Frame(window)
b1=tk.Button(frame2,text="추가",command=add,font=("Arial",13))
b1.grid(row=0,column=0)
b2=tk.Button(frame2,text="그래프",command=data,font=("Arial",13))
b2.grid(row=1,column=0,pady=20)
frame2.pack(pady=10)

window.mainloop()

