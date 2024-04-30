##################### Hard Starting Project ######################
from datetime import datetime
import sys
import random
import os
import pandas as pd

today = (datetime.now().month, datetime.now().day)
df = pd.read_csv("C:\\Users\\FMA\\Documents\\Py\\birthday-wisher-hard-start\\birthdays.csv")
df = df[(df["month"] == today[0]) & (df["day"] == today[1])]
print(df["name"])
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv HINT: https://www.w3schools.com/python/ref_string_replace.asp
if df.empty:
    sys.exit()
else:
    for index, row in df.iterrows():
        n = random.randint(1, 3)
        file_path = f"letter_templates\\letter_{n}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents.replace("[NAME]", row["name"])

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
