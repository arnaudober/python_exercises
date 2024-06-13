import smtplib
import datetime as dt
import random
import constants as constants

with open("quotes.txt", "r") as file:
  quotes = file.readlines()

  now = dt.datetime.now()
  week_day = now.weekday()

  if week_day == 0:
    quote = random.choice(quotes)

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
      connection.starttls()
      connection.login(user=constants.EMAIL_FROM, password=constants.PASSWORD)
      connection.sendmail(from_addr=constants.EMAIL_FROM, to_addrs=constants.EMAIL_TO, msg="Subject:Quote of the week!\n\n" + quote)
