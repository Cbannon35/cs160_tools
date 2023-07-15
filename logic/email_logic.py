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

def create_message(sender, to, subject, message_text, Cc=""):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject
    message['from'] = sender
    message['Cc'] = Cc
    return message

def encode_message(message):
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(message):
    try:
        message = (service.users().messages().send(userId="me", body=message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
        return True
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None
        return False

def email(sender, to, subject, message_text, Cc=""):
    message = create_message(sender, to, subject, message_text, Cc)
    message = encode_message(message)
    return send_message(message)