import datetime

import pandas


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
        for person in data_dict
        if (person["month"], person["day"]) == get_today()
    }

    return today_birthdays


def get_random_template():
    return "Hello [NAME]!"


def replace_variable_in_template(person_name, template):
    return template.replace("[NAME]", person_name)


def send_message(email_address, message):
    print(f"Sending message to {email_address}")
    print(f"Message: {message}")
    return


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
