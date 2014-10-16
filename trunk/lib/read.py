import imaplib


class READ:

    def __init__(self, server, port):
        self.imap = imaplib.IMAP4_SSL(server, int(port))

    def authentication(self, username, password):
        self.imap.login(username, password)

    def read_mail(self, receiver=""):
        self.imap.select('INBOX')
        
        if receiver == "":
            status, response = self.imap.search(None, '(UNSEEN)', 'ALL')
        else:
            status, response = self.imap.search(None, '(UNSEEN)', '(FROM "%s")' % (receiver))
        
        msg = response[0].split()

        """for e_id in msg:
            imap.store(e_id, '+FLAGS', '\Seen')
            """
        data = []

        for e_id in msg:
            _, response = self.imap.fetch(e_id, '(UID BODY[TEXT])')
            data.append(response[0][1])

        return data
