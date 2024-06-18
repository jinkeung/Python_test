import smtplib

#SMTP Library func
'''
SMTP[Simple Mail transfer Protocol](SMTPS [Simple Mail Trnasfer Protocol Secure])
    : 클라이언트와 서버 간의 데이터[메일(텍스트,이미지,파일)] 전송
                                                └MIME 프로토콜

POP3 / IMAP
    : 서버에서 클라이언트로 데이터를 전송(클라이언트 입장에서는 받은 메일?)

SSL[Secure Sockets Layer]: 이전 방식으로 사용, 보안성 결여되어있다.
TLS[Transport Layer Security]: 보안성, 성능적 보완. 
'''
from email.mime.multipart import MIMEMultipart
#분할된 데이터들을 하나로 모아서 전송해주는 역할
from email.mime.text import MIMEText
#텍스트
from email.mime.image import MIMEImage
#이미지
from email.mime.base import MIMEBase
#파일 [타입, 서브타입]

from email.mime.message import MIMEMessage

from email.encoders import encode_base64
#인코딩 라이브러리
import os



server_name="smtp.gmail.com"
server_port=465
user_name="jinkeung1203@gmail.com"
user_pw="oekx kutb dlhr hure"

msg = MIMEMultipart()
msg["Subject"]="제목"
msg["From"]=user_name
msg["To"]=user_name

msg_text=MIMEText("Hello")
msg.attach(msg_text)


with open("pic.jpg","rb") as f:
    msg_img=MIMEImage(f.read())

msg_img.add_header("content-disposition", "attachment", filename="MMM.jpg")
msg.attach(msg_img)

'''
#smtplib.SMTP_SSL : SSL을 통한 데이터 전송
#smtplib.SMTP : TLS를 통한 데이터 전송

SSL=smtplib.SMTP_SSL(server_name, server_port)
SSL.login(user_name, user_pw)
SSL.send_message(msg)
SSL.close()
'''

with smtplib.SMTP(server_name, 587) as TLS:
    TLS.starttls()
    TLS.login(user_name, user_pw)
    TLS.send_message(msg)

'''
smtplib뿐만아니라 뭐든 열고 닫는 작업 필요시!!
=> 왜 열고 닫음? 메모리 누수되면 안되니까
방법 1) 열고 -> close로 닫기 
방법 2) with 써서 작업끝나면 자동으로 종료
'''