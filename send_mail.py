import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'diyorchegg@gmail.com'
password = 'Diyor2003'


def send_mail(text='Email', subject='Hello world', from_email='', to_email=[]):
    assert isinstance(to_email, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_email)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText(f"<p> HELLLLLLLLLLLLLLLOOOOOOOOOOOOOO!!!!!", 'html')
    msg.attach(html_part)
    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg_str)
    server.quite()
