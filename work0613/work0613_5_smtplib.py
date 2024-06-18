import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

'''
#SMTP: 클라이언트-> 서버 메일 전송
 mail: Subject, Content - 텍스트
        +image, video
#MIME: 텍스트, 이미지, 영상 등의 인코딩
'''


server_name="smtp.gmail.com"
server_port=465
user_id="jinkeung1203@gmail.com"
password="oekx kutb dlhr hure"
msg=EmailMessage()
msg["Subject"]="aaa"
msg["From"]=user_id
msg["To"]=user_id
msg.set_content("Hello!")

print(password)
with smtplib.SMTP_SSL(server_name, server_port) as server:
    server.login(user=user_id,password=password)
    server.send_message(msg,user_id,user_id)


