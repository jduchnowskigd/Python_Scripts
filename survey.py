#!/usr/bin/python

"""
This script accepts a json file which is used as a template for a survey,
as well as a list of emails to whom the invite
to this survey should be sent.
"""

import json
import os
import sys
import smtplib
import ssl
import requests

# SINCE SENDING EMAIL INVITATIONS IS A PAID FEATURE IN SURVEYMONKEY
# I DECIDED TO USE AN SMTP SERVER INSTEAD
# AND SEND THE EMAILS FROM THROAWAY GMAIL ACCOUNT

# ACCESS JSON SURVEY TEMPLATE AND LIST OF EMAILS PROVIDED AS ARGUMENTS
NEW_SURVEY = ""
email_list= []
for arg in sys.argv[1:]:
    extension = os.path.splitext(arg)[1]
    if extension == '.json':
        with open(arg, encoding="utf-8") as f:
            NEW_SURVEY=json.load(f)
    else:
        with open(arg, encoding="utf-8") as f:
            email_file = f.readlines()
            for email in email_file:
                email_list.append(email)


with open('config.json', encoding='utf-8') as f:
    json_data = json.load(f)

bearer_token = json_data['Bearer']

client = requests.Session()
client.headers.update({
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {bearer_token}"
})


# POST THE SURVEY
SURVEY_URL = 'https://api.surveymonkey.com/v3/surveys'
survey_json = json.dumps(NEW_SURVEY)
response = client.post(SURVEY_URL, data=survey_json)
response_json = response.json()
surveyid = response_json['id']

# CREATE A WEBLINK TO SHARE
payload = {"type": "weblink"}
url = f"https://api.surveymonkey.com/v3/surveys/{surveyid}/collectors"
collector = client.post(url, json=payload)
response_json = collector.json()
invitation_url = response_json['url']

# SEND INVITATIONS
PORT = 465  # For SSL
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "jan.surveymonkey@gmail.com"  # Enter your address
PASSWORD = "mjapdzxpiqmucgmd"
MESSAGE = f"""\
Subject: Invitation to Survey 

Link to the survey {invitation_url} ."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
    server.login(SENDER_EMAIL, PASSWORD)
    for receiver_email in email_list:
        server.sendmail(SENDER_EMAIL, receiver_email, MESSAGE)
