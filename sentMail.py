import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # 你的邮箱账户
    sender_email = "racoffee33@gmail.com"
    sender_password = "imincoffee@33"

    # 收件人邮箱
    receiver_email = "racoffee33@gmail.com"

    # 创建邮件内容
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "crawler outcome"

    # 读取要发送的文件
    with open("out.txt", "r") as file:
        file_content = file.read()

    # 将文件内容添加到邮件中
    attachment = MIMEText(file_content)
    attachment.add_header("Content-Disposition", "attachment", filename="out.txt")
    message.attach(attachment)

    # 连接到SMTP服务器并发送邮件
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully.")

# 调用函数发送邮件
send_email()

