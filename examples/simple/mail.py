
# enable this by opening this link https://www.google.com/settings/security/lesssecureapps
##
##
##
##
##
##import smtplib
### SMTP_SSL Example
##server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
##server_ssl.ehlo() # optional, called by login()
##server_ssl.login("saivineel6", "ammananass")  
### ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
##server_ssl.sendmail("saivineel6@gmail.com", "saivineel6@gmail.com", "message")
###server_ssl.quit()
##server_ssl.close()
##print 'successfully sent the mail'
##

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromaddr = "saivineel6@gmail.com"
toaddr = "saivineel6@gmail.com"
msg = MIMEMultipart()
msg['From'] = "saivineel6@gmail.com"
msg['To'] = "saivineel6@gmail.com"
msg['Subject'] = "Python email"


body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))

import smtplib
server = smtplib.SMTP("saivineel6@gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("saivineel6@gmail.com", "ammananass")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
