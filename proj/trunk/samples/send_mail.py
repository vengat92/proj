import send

def mail():
    s = send.SEND("smtp.gmail.com", "587")
    s.authentication("clientmail3@gmail.com", "ClientMail123") # username and password
    s.to("clientmail3@gmail.com") # to address
    s.subject()
    s.body("HelloWorld!")
    s.send_mail()

if __name__ == "__main__":
    mail()
