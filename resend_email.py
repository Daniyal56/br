import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def resend_email(name,password,reciver_addr):
    mail_content = f'''
Hey {name},

you can sign in now @ http://192.168.1.89:8501 with email: {reciver_addr} & password: {password}.

For any query you can write us @ scdaniyalalam@gmail.com

Have a Good Day!

Software Channel Pvt. Ltd.
        '''
    sender_addr = 'scdaniyalalam@gmail.com'
    sender_pwd = 'Sidra@123'
    recvr_addr = reciver_addr
    message = MIMEMultipart()
    message['From'] = sender_addr
    message['To'] = reciver_addr
    message['Subject'] = '[Software Channel Pvt. Ltd.] | Verification'
    # message.attach(MIMEText(mail_content))
    message.attach(MIMEText(mail_content))
    #######################################
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.starttls()
    session.login(sender_addr,sender_pwd)
    text = message.as_string()
    session.sendmail(sender_addr,reciver_addr,text)
    session.quit()