import smtplib
from email.message import EmailMessage
import sys
import os
import json
from dotenv import load_dotenv
from test_send_email import email

email_template = json.load(open('email_template.json'))
load_dotenv()
sender_email = os.environ['EMAIL']
sender_password = os.environ['EMAIL_PASS']

def send_emails(approved, rejected, email_type):
    email_type = email_template.get(email_type)
    email_rejected = email_type.get('rejected')
    # email_approved = email_type.get('approved')

    rejected_msg = EmailMessage()
    # approved_msg = EmailMessage()

    rejected_msg['Subject'] = email_rejected.get('subject')
    rejected_msg['From'] = sender_email
    rejected_msg['To'] = 'bannon.c.35@gmail.com'
    rejected_msg.set_content(email_rejected.get('body'))
    rejected_msg['Cc'] = email_rejected.get('CC')

    # print(rejected_msg)

    # s = smtplib.SMTP('localhost')
    # s.send_message(rejected_msg)
    # s.quit()
    # Update the Gmail SMTP server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login("bannon.c.35", sender_password)
        server.send_message(rejected_msg)

# def verbose(approved, rejected, email_type):
#     print("Email type:\n", email_type)
#     print('Sending emails...')
#     print('Approved:')
#     for student in approved:
#         print(student['Name'])
#     print('Rejected:')
#     for student in rejected:
#         print(student['Name'])

def correct_args(args):
    if len(args) != 1:
        print('Incorrect number of args passed')
        return False
    elif args[0] not in ['absence', 'extension']:
        print('Incorrect arg passed')
        return False
    else:
        return True


if __name__ == '__main__':
    args = sys.argv[1:]

    if not correct_args(args):
        print('Usage: python send_email.py [absence/extension]')
        sys.exit(1)
    
    # approved = json.load(open('approved-students.json'))
    # rejected = json.load(open('rejected-students.json'))
    approved, rejected = True, False
    email_type = args[0]
    # verbose(approved, rejected, email_type)
    send_emails(approved, rejected, email_type)
    

    
