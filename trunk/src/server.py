import send
import read
import re
import os

def init():
    global re
    global s

    re = read.READ("imap.gmail.com", "993")
    s = send.SEND("smtp.gmail.com", "587")


def authentication():
    fo = open("pass.txt", "r+") #pass.txt contains username and password
    tmp = fo.readlines()
    username = tmp[0]
    password = tmp[1]

    re.authentication(username, password)
    s.authentication(username, password)


def check_mail():
    re.read_mail("YYYY") #YYYY to address
    bashcmd = "scc " + str(re.path)
    os.system(bashcmd)

def send_mail():
    s.to("YYYY") #YYYY to address
    s.subject()
    s.content()
    s.send_mail(str(re.dir)+"/error.txt")
    
if __name__ == "__main__":
    init()
    authentication()
    check_mail()
    send_mail()

