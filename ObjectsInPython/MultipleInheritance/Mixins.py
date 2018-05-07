class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class MailSender:
    def send_mail(self,message):
        print("Sending mail to" + self.email)
        #Add e-mail logic here

#The use of it is when we inherit Contact and MailSender

class EmailableContact(Contact, MailSender):
    pass

    
