import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def write_log(content):
    fo = open("/home/fqyang/out.txt", "a+")
    str = content
    fo.write( str + "\n")

def email_test1():

    Sender = "854143470@qq.com"
    #Password = os.environ.get('QQ_IMAP_CODE')
    Password="XXYY"
    Receiver = "fqyyang@gmail.com"

    msg = MIMEText("时间：10:08 PM")
    msg["Subject"] = "服务器Swarm-worker1宕机，现在已自动切换到Swarm-manager!"
    msg["From"] = Sender
    msg["To"] = Receiver
    
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(Sender, Password)
        s.sendmail(Sender, Receiver, msg.as_string())
        s.quit()
        print("Success!")
    except smtplib.SMTPException as e:
        print("Falied! Error is %s" % e)


if __name__ == "__main__":
    email_test1()

