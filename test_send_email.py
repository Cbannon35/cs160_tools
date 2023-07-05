import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

service = build('gmail', 'v1', credentials=creds)

def create_message(sender, to, Cc, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject
    message['from'] = sender
    message['Cc'] = Cc
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(message):
    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None

def email(sender, to, Cc, subject, message_text):
    message = create_message(sender, to, Cc, subject, message_text)
    send_message(message)

if __name__ == '__main__':
    message = create_message('bannon.c.35@berkeley.edu', 
                             'bannon.c.35@gmail.com', 
                             'bannon.c.35@berkeley.edu', 
                             'Email test pt 2', 
                             'This is the body of the email')
    
    send_message(message)



# def test():
#     message = MIMEText('This is the body of the email')
#     message['to'] = 'bannon.c.35@gmail.com'
#     message['subject'] = 'Email test pt 2'
#     message['from'] = 'bannon.c.35@berkeley.edu'
#     message['Cc'] = 'bannon.c.35@berkeley.edu'
#     create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

#     try:
#         message = (service.users().messages().send(userId="me", body=create_message).execute())
#         print(F'sent message to {message} Message Id: {message["id"]}')
#     except HTTPError as error:
#         print(F'An error occurred: {error}')
#         message = None
