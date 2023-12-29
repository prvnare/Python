# program to send the email from gmail
from email.message import EmailMessage;
import smtplib;
import ssl;

class Email:
    def __init__(self, sender, pwd, reciever, subject, body):
        self.__sender = sender;
        self.__pwd = pwd;
        self.__reciever = reciever;
        self.__subject  = subject;
        self.__body = body;
    
    def getSender(self):
        return self.__sender;

    def getReciever(self):
        return self.__reciever;

    def getSubject(self):
        return self.__subject;

    def getBody(self):
        return self.__body;

    def getPWD(self):
        return self.__pwd;

def sendEmail(getEmailDetails):
    print('sending an email using decorator');
    def send(email):
        email_message = EmailMessage();
        email_message['From'] = email.getSender();
        email_message['To'] = email.getReciever();
        email_message['subject'] = email.getSubject();
        email_message.set_content(email.getBody());
        ssl_context = ssl.create_default_context();
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = ssl_context) as smtp :
            try: 
                smtp.login(email.getSender(), email.getPWD());
                smtp.sendmail(email.getSender(), email.getReciever(), email_message.as_string());
            except Exception as exception: 
                print('issue in sending an email', exception);
        getEmailDetails();
    return send;
 
@sendEmail
def send_email_details(email):
    print('Email has sent');
    
if __name__ == '__main__':
    send_email_details(Email(None,None,None,None,None));