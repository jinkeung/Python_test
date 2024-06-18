import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
#자체적으로 이미지, 텍스트 보낼 수 있는 모든 라이브러리

from email.mime.text import MIMEText        #텍스트
from email.mime.image import MIMEImage      #이미지
from email.mime.base import MIMEBase        #파일 전송
from email.mime.message import MIMEMessage  #첨부파일(텍스트 제외 다른것들에 필요함)

from email.encoders import encode_base64    #인코딩
from email.mime.multipart import MIMEMultipart #데이터 전송 시 여러파일 하나로 묶는데 사용

msg=MIMEMultipart()
id="jinkeung1203@gmail.com"
pw="oekx kutb dlhr hure"
msg['From']=id
msg['To']=pw
msg['Subject']="제목"

text=MIMEText("텍스트")
msg.attach(text)

from test import image_down
if __name__=="__main__":
    image_down("https://cdn.imweb.me/thumbnail/20240607/b67869149093a.jpg")


with open("img.jpg","rb") as f:
    image=MIMEImage(f.read())

image_data=MIMEMessage(image)
msg.attach(image_data)





with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(id,pw)
    server.send_message(msg,id,id)

import tkinter as tk
from PIL import Image, ImageTk
import os


home=tk.Tk()
home.geometry('500x500')
canvas=tk.Canvas(home,width=500,height=500)
a=ImageTk.PhotoImage(Image.open("img.jpg"))
canvas.create_image(0,0,image=a,anchor=tk.NW)
canvas.pack()
home.mainloop()
