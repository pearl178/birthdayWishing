##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "charbat.serikbol@gmail.com"
password = '117878Tian'
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month_now = now.month
day_now = now.day
data = pd.read_csv("birthdays.csv")
df = pd.DataFrame(data)
for index, row in df.iterrows():
    if row.month == month_now and row.day == day_now:
        receive_name = row['name']
        receive_email = row['email']

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter_num = random.randint(1,3)
with open(f"letter_templates/letter_{letter_num}.txt") as letter_file:
    sample_letter = letter_file.read()
letter_to_send = sample_letter.replace('[NAME]', receive_name)
letter_to_send = letter_to_send.replace('Angela', 'Pearl')
# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receive_email,
        msg=f"Subject:Happy Birthday!\n\n {letter_to_send}"
    )



