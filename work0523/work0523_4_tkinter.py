import tkinter as tk    #창[window,form] 만들기, 표준 GUI 구현 내부라이브러리

root = tk.Tk()                              #window 창
root.title("제목제목제목")                    #제목
root.resizable(True, True)      #사이즈조절 default: False,False
root.geometry("600x600+500+300")            #width x height x x축 + y축

'''추가
tk.Button()         이벤트 동작
tk.Label()          subtitle
tk.Entry()          input tag
'''
'''
label=tk.Label(master=root, text="Label text",borderwidth=1,relief="solid")
#label.pack()                                     #pack: 하나의 행을 기준으로 상대적 위치
label.grid(row=0, column=0)                       #grid: 격자무늬, 행과 열을 기준으로 상대적 위치

label2=tk.Label(master=root, text="Label text2",bg="pink", fg="white",borderwidth=1,relief="solid")
label2.grid(row=0, column=1)
#label2.pack(side="left", fill=tk.BOTH, expand=True, padx=100, pady=100, ipadx=100,ipady=100)

label3=tk.Label(root, text="Label text3", bg="blue", fg="white", width=20, borderwidth=1,relief="solid")
label3.grid(row=1, column=0, columnspan=2)        #span: 셀 병합


label4=tk.Label(root,text="Label text 44444",bg="white",borderwidth=1,relief="solid")
label4.place(x=0,y=0)                             # 절대 위치, pack(), grid()와 혼용
'''


def click():
    label.configure(text=entry.get())

label=tk.Label(root,text="클릭 전")
label.pack()

button=tk.Button(root,text="BUTTON", command=click)      #command: ==onclick
button.pack()

entry=tk.Entry(root)
entry.pack()

list=tk.Listbox(root)
list.insert(0,"Hello")
list.insert("end","World")
list.insert("end","Robot")
list.pack()

import oracledb as db
con = db.connect(dsn="192.168.0.35:1521/xe", user="c##test", password="1234")
cursor=con.cursor()
cursor.execute("select * from pytest")

list2=tk.Listbox(root)
for i in cursor:
    list2.insert("end",i)
list2.pack()




root.mainloop()                 #무한루프 (돌려놔야 창이 유지됨)


