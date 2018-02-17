import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config import config
from scrape.ScrapeExceptions import ScrapeExceptions
# Note: Don't call this file email.py becaue that conflicts with something in smtplib

class Email:

	def __init__(self, emailClass):
		self.emailClass = emailClass

	def send(self):
		try:
			gmailUser = config.this_account_email
			gmailPassword = config.this_account_email_password
			recipient = self.emailClass.recipient
			message = self.emailClass.message

			msg = MIMEMultipart()
			msg['From'] = gmailUser
			msg['To'] = recipient
			msg['Subject'] = self.emailClass.subject
			msg.attach(MIMEText(message))

			if self.emailClass.attachmentAvailable:
				with open(self.emailClass.attachment, "rb") as file:
					part = MIMEApplication(file.read(), self.emailClass.attachmentName)
					part['Content-Disposition'] = 'attachment; filename="{}"'.format(self.emailClass.attachmentName)
					msg.attach(part)


			mailServer = smtplib.SMTP('smtp.gmail.com', 587)
			mailServer.ehlo()
			mailServer.starttls()
			mailServer.ehlo()
			mailServer.login(gmailUser, gmailPassword)
			mailServer.sendmail(gmailUser, recipient, msg.as_string())
			mailServer.close()
		except:
			raise ScrapeExceptions.EmailNotificationError()











