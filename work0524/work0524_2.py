#tkinter [표준 GUI 구현 라이브러리], matplotlib[GUI 그래프 구현 라이브러리]
import tkinter as tk
from tkinter import ttk

window=tk.Tk()     #form, window창 구현
window.title("0524 window")
window.geometry("500x750+900+100")
window.resizable(True,False)

tk.Toplevel()




f_top=tk.Frame(window)
l_title=tk.Label(f_top,text="제목",relief="solid",font=("Arial",30))
l_title.pack(ipadx=50,ipady=10,pady=50)
f_top.pack(side=tk.TOP)


f_main=tk.Frame(window)
l_id=tk.Label(f_main,text="ID",font=("Arial",15))
l_id.grid(row=0,column=0,pady=10)
e_id=tk.Entry(f_main,width=15,font=("Arial",15))
e_id.grid(row=0,column=1)

l_pw=tk.Label(f_main,text="PW",font=("Arial",15))
l_pw.grid(row=1,column=0,pady=10)
e_pw=tk.Entry(f_main,width=15,font=("Arial",15))
e_pw.grid(row=1,column=1)

l_name=tk.Label(f_main,text="Name",font=("Arial",15))
l_name.grid(row=2,column=0,pady=10,padx=10)
e_name=tk.Entry(f_main,width=15,font=("Arial",15))
e_name.grid(row=2,column=1)




b_submit=tk.Button(f_main,text="Submit",font=("Arial",15),width=20)
b_submit.grid(row=3,column=0,columnspan=2,pady=10)

f_main.pack(anchor="w")

tv=ttk.Treeview(window,columns=("Name","PW"),displaycolumns=("Name","PW"))
# columns = "ID"는 기준 (default로 하나는 만들어짐) 가지고 있는 컬럼
# displyacolumns= ("Name","Pw") :default 보여줄 컬럼

tv.column("Name",width=80)      #지정한 컬럼에 대한 옵션 등을 조정
tv.column("PW",width=200)

tv.heading("#0",text="ID",anchor='w')      #컬럼 제목 표시 "#0"==0번째
tv.heading("Name",text="Name",anchor='e')
tv.heading("PW",text="PW",anchor='w')

id =tv.insert("","end",text="A")
tv.insert(id,"end",values=['A','B'])




tv.pack()

f_bot=tk.Frame(window,bg="pink")
l_bot=tk.Label(f_bot,text="안녕하세요, 감사해요, 잘있어요 다시 만나요",bg="pink",font=("",15))
l_bot.pack(side="right",anchor="s")
f_bot.pack(side=tk.BOTTOM,fill="x",ipady=40)




window.mainloop()