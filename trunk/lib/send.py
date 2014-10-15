import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SEND:
    
    def __init__(self, server, port):
        """Initialize SMTP server and the port address"""
        self.ser = smtplib.SMTP(server, int(port))
        self.ser.ehlo()
        self.ser.starttls()
        self.ser.ehlo()

    def authentication(self, username, password):
        """Authenticating sender username and the password"""
        self.ser.login(username, password)
        self.from_addr = username

    def to(self, to_addr):
        """Initialize receiver address"""
        self.to_addr = to_addr

    def subject(self, subject=""):
        self.subject = subject

    def content(self, content=""):
        self.content = content

    def send_mail(self, filename=""):
        msg = MIMEMultipart()
        msg["From"] = self.from_addr
        msg["To"] = self.to_addr
        msg["Subject"] = self.subject
        body = MIMEMultipart('alternative')
        body.attach(MIMEText(self.content, "plain"))
        msg.attach(body)
        msg.attach(MIMEText(file(filename).read()))
        self.ser.sendmail(self.from_addr, self.to_addr, msg.as_string())
