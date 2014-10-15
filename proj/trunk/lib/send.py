import smtplib


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

    def body(self, body=""):
        self.body = body

    def send_mail(self):
        headers = "\r\n".join(["from: " + self.from_addr,
                       "subject: " + self.subject,
                       "to: " + self.to_addr,
                       "mime-version: 1.0",
                       "content-type: text/html"])
        content = headers + "\r\n\r\n" + self.body
        self.ser.sendmail(self.from_addr, self.to_addr, content)
