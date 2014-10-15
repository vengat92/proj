#!/usr/bin/python
def gmail_checker(username,password):
  import imaplib,re
  i=imaplib.IMAP4_SSL('imap.gmail.com')
  try:
    i.login(username,password)
    x,y=i.status('INBOX','(MESSAGES UNSEEN)')
    messages=int(re.search('MESSAGES\s+(\d+)',y[0]).group(1))
    unseen=int(re.search('UNSEEN\s+(\d+)',y[0]).group(1))
    return (messages,unseen)
  except:
    return False,0
messages,unseen = gmail_checker('clientmail3@gmail.com','ClientMail123')
print "%i messages, %i unseen" % (messages,unseen)
