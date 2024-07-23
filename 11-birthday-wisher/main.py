import smtplib
import datetime as dt
import random
import constants as constants

# TODO:
# 1. Open the CSV file to get the information.
# 2. For each birthday that is today:
#   a. Randomly choose a template file in /letter_templates.
#   b. Replace the variable with the name of the CSV file.
#   c. Send the message to the email from the CSV file.