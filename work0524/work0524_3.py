import tkinter as tk
from tkinter import ttk
import oracledb as db






#HOME - ID, PW, 로그인버튼, 회원가입 버튼
home=tk.Tk()
home.geometry('500x500')
home.title('HOME')

f_home=tk.Frame(home)
l_id=tk.Label(f_home,text='ID',font=('Arial',15),pady=5)
l_id.grid(row=0,column=0)
e_id=tk.Entry(f_home,font=('Arial',15))
e_id.grid(row=0,column=1)
l_pw=tk.Label(f_home,text='PW',font=('Arial',15),pady=5)
l_pw.grid(row=1,column=0)
e_pw=tk.Entry(f_home,font=('Arial',15))
e_pw.grid(row=1,column=1)


#LOGIN - 로그인확인, 데이터보여주기
def login():
    con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
    cursor=con.cursor()
    cursor.execute('select pw from users where id=:id',id=e_id.get())

    if cursor.fetchone()[0]==e_pw.get():
        print("로그인 성공")
        data_show()
    else: print("로그인 실패")

    cursor.close()
    con.close()
def data_show():
    data=tk.Toplevel()
    data.geometry('1000x500')
    data.title('DATA')

    tv=ttk.Treeview(data,columns=("pw","name"))
    tv.column("pw")
    tv.column("name")



    con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
    cursor=con.cursor()
    cursor.execute('select * from users')

    li = [i[0] for i in cursor.description]

    tv.heading("#0",text=li[0])
    tv.heading("pw",text=li[1])
    tv.heading("name",text=li[2])

    for i in cursor.fetchall():
        tv.insert("","end",text=i[0],values=[i[1],i[2]])

    tv.pack(pady=30)

    def focus():
        print(tv.get_children(tv.focus()))

    b_focus=tk.Button(data,text="focus",command=focus)
    b_focus.pack()



    cursor.close()
    con.close()

b_login=tk.Button(f_home,command=login, text="로그인",font=('Arial',15),width=25)
b_login.grid(row=2,column=0,columnspan=2)



#JOIN - ID,PW,NAME, 회원가입완료 버튼
def join_main():
    join=tk.Toplevel()
    join.title("JOIN")
    join.geometry("500x500")

    f_join=tk.Frame(join)
    l_id=tk.Label(f_join,text='ID',font=('Arial',15),pady=5)
    l_id.grid(row=0,column=0)
    e_id=tk.Entry(f_join,font=('Arial',15))
    e_id.grid(row=0,column=1)
    l_pw=tk.Label(f_join,text='PW',font=('Arial',15),pady=5)
    l_pw.grid(row=1,column=0)
    e_pw=tk.Entry(f_join,font=('Arial',15))
    e_pw.grid(row=1,column=1)
    l_name=tk.Label(f_join,text='NAME',font=('Arial',15),pady=5)
    l_name.grid(row=2,column=0)
    e_name=tk.Entry(f_join,font=('Arial',15))
    e_name.grid(row=2,column=1)


    def join_end():
        con=db.connect(dsn="192.168.0.35:1521/xe",user="c##test",password="1234")
        cursor=con.cursor()
        cursor.execute('insert into users values (:id,:pw,:name) '
                       ,id=e_id.get(),pw=e_pw.get(),name=e_name.get())
        con.commit()
        cursor.close()
        con.close()
        join.destroy()


    b_login=tk.Button(f_join,command=join_end,text="회원가입 완료",font=('Arial',15),width=25)
    b_login.grid(row=3,column=0,columnspan=2)

    f_join.pack(pady=50)

    join.mainloop()

b_join=tk.Button(f_home, command=join_main,text="회원가입",font=('Arial',15),width=25)
b_join.grid(row=3,column=0,columnspan=2)

f_home.pack(pady=50)



home.mainloop()
