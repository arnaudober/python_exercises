import datetime
import random
import smtplib

import pandas

from constants import *


def get_today():
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    return month, day


def get_birthdays_to_celebrate():
    data = pandas.read_csv("birthdays.csv")
    data_dict = data.to_dict(orient="records")
    today_birthdays = {
        (person["month"], person["day"]): {
            "name": person["name"],
            "email": person["email"],
        }
        for birthday in data_dict
        if (birthday["month"], birthday["day"]) == get_today()
    }

    return today_birthdays


def get_random_template():
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, "r") as f:
        return f.read()


def replace_variable_in_template(person_name, template):
    return template.replace("[NAME]", person_name)


def send_message(email_address, message):
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_FROM, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_FROM,
            to_addrs=email_address,
            msg=f"Subject:Happy birthday!\n\n{message}",
        )


# TODO:
# a. Randomly choose a template file in /letter_templates.
# b. Replace the variable with the name of the CSV file.
# c. Send the message to the email from the CSV file.
birthdays_to_celebrate = get_birthdays_to_celebrate()
for key in birthdays_to_celebrate:
    person = birthdays_to_celebrate[key]
    name = person["name"]
    email = person["email"]
    random_template = get_random_template()
    emailToSend = replace_variable_in_template(name, random_template)
    send_message(email, emailToSend)
