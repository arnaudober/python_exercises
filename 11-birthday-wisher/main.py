import smtplib
import constants as constants

with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
  connection.starttls()
  connection.login(user=constants.EMAIL_FROM, password=constants.PASSWORD)
  connection.sendmail(from_addr=constants.EMAIL_FROM, to_addrs=constants.EMAIL_TO, msg="Subject:Hello\n\nThis is the body of my email")
