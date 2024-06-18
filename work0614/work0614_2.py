from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

import pynput
import smtplib


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.message import MIMEMessage
import tkinter.messagebox as mbox
import os
#tk 창을 통해 google과 naver로 전송하는 smtp 구분 작업을 수행 [Checkbutton] 이용하여 smtp서버에 접근
#해당 접근이 완료시에, 기존의 창을 대체하여 아이디와 비밀번호를 입력하는 공간 구현

#만약 해당 로그인이 정상적인 상태면 새로운 창과 함께 제목과 본문, To_addr [아이디는 라벨, 주소는 combobox]
# 이미지의 경로를 작성하는 label 구현
#label 옆에는 버튼을 명시하여 이미지의 경로를 선택할 수 있는 창을 구현.
#만약 해당파일을 선택하여 이미지를 열게되면 해당 내용은 이미지 경로 Label에 적재
#최하단 버튼 메일 전송버튼, Enter 입력시 해당버튼 작동 되도록

#로그인 실패 상태면 Except 오류에 대한 데이터를 알림창을 통해 구현

print(os.getcwd())


def mailpage():


    def sendmail():


        try:
            msg=MIMEMultipart()
            msg['From']=e_id.get()
            msg['To']=e_to.get()+c_to.get()
            msg['Subject']=e_title.get()

            msg.attach(MIMEText(e_content.get()))

            if os.path.exists(l_img_add.get()):
                with open(l_img_add.get(), 'rb') as fp:
                    msg.attach(MIMEImage(fp.read()))

                server.send_message(msg)
                server.close()
                mbox.showinfo("END","메일 전송 완료")
                mail.destroy()
                login.destroy()
                home.destroy()
            else:
                mbox.showerror("FAIL","이미지파일 없음")
        except Exception as e:
            mbox.showerror("FAIL",str(e))




    def imgpick():
        img_add=filedialog.askopenfilename()
        l_img_add.insert(tk.END, img_add)


    mail=tk.Toplevel()
    mail.title("MAIL")
    mail.geometry("1000x500")
    f_mail=tk.Frame(mail)
    l_title=tk.Label(f_mail, text="제목",font="Arial 13")
    l_title.grid(row=0, column=0, pady=10)
    e_title=tk.Entry(f_mail)
    e_title.grid(row=0, column=1, pady=10)
    l_content=tk.Label(f_mail,text="내용",font="Arial 13")
    l_content.grid(row=1, column=0, pady=10)
    e_content=tk.Entry(f_mail)
    e_content.grid(row=1, column=1, pady=10)
    l_to=tk.Label(f_mail, text="TO",font="Arial 13")
    l_to.grid(row=2, column=0, pady=10)
    e_to=tk.Entry(f_mail)
    e_to.grid(row=2, column=1, pady=10)
    c_to=ttk.Combobox(f_mail,font="Arial 13")
    c_to.grid(row=2,column=2, pady=10)
    c_to.config(values=["@gmail.com","@naver.com","@daum.net"])
    c_to.set("@gmail.com")
    l_img=tk.Label(f_mail,text="IMAGE",font="Arial 13")
    l_img.grid(row=3, column=0, pady=10)
    l_img_add=tk.Entry(f_mail,font="Arial 13")
    l_img_add.grid(row=3, column=1, pady=10)
    b_img_add=tk.Button(f_mail,text="이미지 찾기",font="Arial 13",command=imgpick)
    b_img_add.grid(row=3, column=2, pady=10)
    b_send=tk.Button(f_mail, text="메일 전송", font="Arial 13",command=sendmail)
    b_send.grid(row=4, column=1, pady=10)
    f_mail.pack(pady=10)


def loginprocess():
    try:
        server.login(e_id.get(),e_pw.get())
        mailpage()
    except Exception as e:
        mbox.showerror("ERROR",str(e))
        print(e)

def loginpage():
    global e_id, e_pw, login
    login=tk.Toplevel()
    login.geometry('300x300')
    login.title('Login')
    f_login=tk.Frame(login)
    l_id=tk.Label(f_login, text="ID",font=("Arial",13))
    l_id.grid(row=0, column=0,pady=10)
    e_id=tk.Entry(f_login,font=("Arial",13))
    e_id.grid(row=0, column=1)
    l_pw=tk.Label(f_login, text="PW",font=("Arial",13))
    l_pw.grid(row=1, column=0,pady=10)
    e_pw=tk.Entry(f_login,font=("Arial",13),show="*")
    e_pw.grid(row=1, column=1)
    b_login=tk.Button(f_login, text="Login", font=("Arial",13), command=loginprocess)
    b_login.grid(row=2, column=0,columnspan=2,pady=10)
    f_login.pack(pady=10)

def connect():
    global server
    google=google_var.get()
    naver=naver_var.get()
    if google==1 and naver==1:
        mbox.showerror("ERROR","하나만 선택해주세요")
    elif google==0 and naver==0:
        mbox.showerror("ERROR","선택해주세요")
    elif google==1:
        try:
            server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
            loginpage()
        except Exception as e:
            print(e)
    elif naver==1:
        try:
            server=smtplib.SMTP_SSL('smtp.naver.com', 465)
            loginpage()
        except Exception as e:
            print(e)

if __name__=="__main__":
    home=tk.Tk()
    home.geometry('500x500')
    home.title('HOME')
    f_home=tk.Frame(home)

    google_var=tk.IntVar()
    naver_var=tk.IntVar()
    c_google=tk.Checkbutton(master=f_home,text="google",variable=google_var,font="Arial 13")
    c_google.pack(pady=10)
    c_naver=tk.Checkbutton(master=f_home,text="naver",variable=naver_var,font="Arial 13")
    c_naver.pack(pady=10)
    b_select=tk.Button(f_home,text="서버 접근",font="Arial 10",command=connect)
    b_select.pack(pady=10)
    f_home.pack(pady=10)
    home.mainloop()

