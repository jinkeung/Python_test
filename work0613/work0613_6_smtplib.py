import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

'''
#SMTP: 클라이언트-> 서버 메일 전송
 mail: Subject, Content - 텍스트
        +image, video
#MIME: 텍스트, 이미지, 영상 등의 인코딩
'''
import tkinter as tk
import tkinter.messagebox as mbox


def send():
    msg=EmailMessage()
    msg["Subject"]=e_sub.get()
    msg["From"]=e_id.get()
    msg["To"]=e_id.get()

def login():
    global id, pw, server_name, server_port
    id=e_id.get()
    pw=e_pw.get()
    server_name="smtp.gmail.com"
    server_port=465
    try:
        with smtplib.SMTP_SSL(server_name, server_port) as server:
            server.login(id,pw)

        global e_sub, e_con

        mail=tk.Toplevel()
        mail.geometry('500x300')
        f_mail=tk.Frame(mail)
        l_sub=tk.Label(f_mail,text='Subject',font="Arial 13")
        l_sub.grid(row=0,column=0,pady=10)
        e_sub=tk.Entry(f_mail)
        e_sub.grid(row=0,column=1,pady=10)
        l_con=tk.Label(f_mail,text='Content',font="Arial 13")
        l_con.grid(row=1,column=0,pady=10)
        e_con=tk.Entry(f_mail)
        e_con.grid(row=1,column=1,pady=10)
        b_mail=tk.Button(f_mail,text='Send mail',command=send)
        b_mail.grid(row=2,column=0,columnspan=2,pady=10)
        f_mail.pack(pady=10)
    except Exception:
        mbox.showerror("ERROR","로그인 실패")

home=tk.Tk()
home.geometry('500x300')
f_home=tk.Frame(home)
l_id=tk.Label(f_home,font="Arial 13",text="ID")
l_id.grid(row=0,column=0,pady=10)
e_id=tk.Entry(f_home,font="Arial 13")
e_id.grid(row=0,column=1,pady=10)
l_pw=tk.Label(f_home,font="Arial 13",text="PW")
l_pw.grid(row=1,column=0,pady=10)
e_pw=tk.Entry(f_home,font="Arial 13",show="*")
e_pw.grid(row=1,column=1,pady=10)
b_login=tk.Button(f_home,text="Login",font="Arial 13",command=login)
b_login.grid(row=2,column=0,columnspan=2,pady=10)
f_home.pack()
home.mainloop()

