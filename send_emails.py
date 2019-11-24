# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# fromEmail - your email
# email - passing emails from csv
# subject - the email subject line
# message - pass in your email message


def send_email(fromEmail, email, subject, message):
    message = Mail(
        from_email=fromEmail,
        to_emails=email,
        subject=subject,
        html_content=message)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


with open('emails.csv', 'r') as emails:
    count = 1
    for email in emails:
        print(str(count) + ': ', email)
        send_email('your-email', email, 'your-subject-line', 'your-message')
        count = count + 1
