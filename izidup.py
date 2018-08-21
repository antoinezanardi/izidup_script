import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Insert in this array all the APIs or domain you want to test. The existed values are just examples
urls = []

# Choose the ways to warn you if the above URLs doesn't respond 200 (you can choose several ones)
useSlack = True
useMail = True

# If you choose the mail solution, please provide your mail credentials below
host = ""
port = 0
login = ""
password = ""

# Insert in this array the list of people email address who needs to be warned
mails = []

# If you choose the Slack solution, please provide your webhook URL below
slackWebhookURL = ""

def main():
	for url in urls:
		try:
			r = requests.get(url);
		except requests.exceptions.RequestException as e:
			r = None
		generateMessage(r, url)

def generateMessage(r, url):
	message = ""
	if r is None:
		message = "The connexion with the URL \"" + url + "\" couldn't be established"
	elif r.status_code != 200:
		message = "The URL \"" + url + "\" answered with code " + str(r.status_code) + "\n"
		message += str(r.json())
	if message != "":
		if useSlack == True:
			sendSlackMsg(message)
		if useMail == True:
			sendMail(message)


def sendSlackMsg(message):
	requests.post(slackWebhookURL, json={"text": message})

def sendMail(message):
	toaddr = ""
	for mail in mails:
		toaddr += mail
	msg = MIMEMultipart()
	msg['From'] = "izidup@script.com"
	msg['To'] = toaddr
	msg['Subject'] = "[IZIDUP]: Oops, something's wrong"
	msg.attach(MIMEText(message, 'plain'))
 
	server = smtplib.SMTP_SSL(host, port)
	server.login(login, password)
	text = msg.as_string()
	server.sendmail(msg['From'], toaddr, text)
	server.quit()

if __name__== "__main__":
  	main()