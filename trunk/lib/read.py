import imaplib
import os
import shutil
import email


class READ:

    def __init__(self, server, port):
        self.imap = imaplib.IMAP4_SSL(server, int(port))
        self.path = ""
        self.dir = ""

    def authentication(self, username, password):
        self.imap.login(username, password)

    def read_mail(self, receiver=""):
        self.imap.select('INBOX')
        
        if receiver == "":
            status, response = self.imap.search(None, '(UNSEEN)', 'ALL')
        else:
            status, response = self.imap.search(None, '(UNSEEN)', '(FROM "%s")' % (receiver))
        
        msg = response[0].split()

        for e_id in msg:
            typ, response = self.imap.fetch(e_id, '(RFC822)')
            data = response[0][1]
            mail = email.message_from_string(data)
        
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = str(part.get_filename())
                dirname = os.path.splitext(os.path.basename(filename))[0]

                if os.path.exists(dirname):
                    shutil.rmtree(dirname)
                    os.makedirs(dirname)
                else:
                    os.makedirs(dirname)

                self.path = dirname + "/" + filename
                self.dir = dirname

                fp = open(self.path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
