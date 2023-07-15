import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


approved_students_path = os.path.join(current_dir, 'students/approved_students.json')
rejected_students_path = os.path.join(current_dir, 'students/rejected_students.json')
emails_path = os.path.join(current_dir, 'generated_emails/emails.json')
email_template_path = os.path.join(current_dir, 'generated_emails/email_template.json')


### Students ###
def read_students():
    approved = json.load(open(approved_students_path))
    rejected = json.load(open(rejected_students_path))
    return approved['students'], rejected['students'], approved['flag']

def write_students(approved, rejected, flag):
    json.dump({'students': approved, 'flag': flag}, open(approved_students_path, 'w'))
    json.dump({'students': rejected, 'flag': flag}, open(rejected_students_path, 'w'))

def clear_students():
    write_students([], [], None)

### Emails ###
def read_emails() -> tuple[list, str]:
    emails = json.load(open(emails_path))
    return emails['emails'], emails['flag']

def write_emails(emails, flag) -> None:
    json.dump({"emails": emails, "flag": flag}, open(emails_path, 'w'))

def clear_emails() -> None:
    write_emails([], None)

def read_email_template(flag: str) -> dict:
    return json.load(open(email_template_path))[flag]