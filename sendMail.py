import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def sendMail(title,Content):
    sender = '1150169485@qq.com'
    #receivers = '651885427@qq.com'
    receivers = '2934409798@qq.com'
    #receivers = '1355782779@qq.com'
    message = MIMEMultipart('related')
    subject = title
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receivers
    #content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>','html','utf-8')
    content = MIMEText(Content,'html','utf-8')
    message.attach(content)

    file=open("G:\\python\\Video\\TengXun\\timg.jpg", "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    message.attach(img)

    try:
        server=smtplib.SMTP_SSL("smtp.qq.com",465)
        server.login(sender,"hgkqpdemucyjiffc")
        server.sendmail(sender,receivers,message.as_string())
        server.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    content='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<img src="http://cms-bucket.nosdn.127.net/2018/12/10/7cc7ebe5f0ae4af3b1738f38a79405c8.jpg" alt="">
</body>
</html>
    '''
    sendMail(content)
