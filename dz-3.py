import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import imaplib


class Email:
    def __init__(self):
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.l = 'laitkilla@gmail.com'
        self.passwORD = 'msumcfzz342511m'
        self.subject = 'Subject'
        self.recipients = ['troyan_rus@mail.ru']
        self.message = 'Message'
        self.header = None


    def send_message(self):
        # send message
        self.msg = MIMEMultipart()
        self.msg['From'] = self.l
        self.msg['To'] = ', '.join(self.recipients)
        self.msg['Subject'] = self.subject
        self.msg.attach(MIMEText(self.message))

        self.ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        self.ms.ehlo()
        # secure our email with tls encryption
        self.ms.starttls()
        # re-identify ourselves as an encrypted connection
        self.ms.ehlo()

        self.ms.login(self.l, self.passwORD)
        self.ms.send_message(self.msg)

        self.ms.quit()
        # send end

    def reсieve(self):
        self.mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        self.mail.login(self.l, self.passwORD)
        self.mail.list()
        self.mail.select("inbox")
        self.criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        self.result, self.data = self.mail.uid('search', None, self.criterion)
        assert self.data[0], 'There are no letters with current header'
        self.latest_email_uid = self.data[0].split()[-1]
        self.result, self.data = self.mail.uid('fetch', self.latest_email_uid, '(RFC822)')
        self.raw_email = self.data[0][1]
        self.raw = self.raw_email.decode('UTF-8')
        self.email_message = email.message_from_string(self.raw_email)
        self.mail.logout()


test = Email()
test.reсieve()