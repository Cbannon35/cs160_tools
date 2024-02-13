import sys
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()


# Please pass in the row from spreadsheet into the command line
# Please put the assignment in quotes if it has spaces
def main():

    date = sys.argv[1]
    time = sys.argv[2]
    email = sys.argv[3]
    first_name = sys.argv[4]
    last_name = sys.argv[5]
    assignment = sys.argv[6]
    due_date = sys.argv[7]
    extension_days = sys.argv[8]
    extension_date = sys.argv[9]
    dsp = sys.argv[10]
    # reason = sys.argv[11] not needed

    flag = True
    long = False

    # auto accept dsp requesting extension under 4 days
    if dsp != "Yes" and int(extension_days) <= 4:
        while True:
            user_input = input("Accept Extension? y or n ")
            if user_input.lower() == 'y':
                flag = True
                break
            elif user_input.lower() == 'n':
                flag = False
                break
            else:
                print("Please enter 'y' or 'n'")
                print('')

        while True:
            user_input = input("Should student schedule time to meet?")
            if user_input.lower() == 'y':
                long = True
                break
            elif user_input.lower() == 'n':
                long = False
                break
            else:
                print("Please enter 'y' or 'n'")
                print('')

    else:
        long = True
    
    email_body = read_email(flag, long)
    email_body = email_body.replace('~NAME~', first_name)
    email_body = email_body.replace('~ASSIGNMENT~', assignment)
    email_body = email_body.replace('~DATE~', extension_date)
    email_body = email_body.replace('~DUE_DATE~', due_date)
    email_body = email_body.replace('~DAYS~', extension_days)

    subject = "CS160 Extension Request"
    cc = os.getenv('CC_EMAIL')
    send_email(subject, email, cc, email_body)

def send_email(subject, to, cc, body):
    '''Opens the apple mail app with fields filled out'''
    mailto_url = f"mailto:{to}?cc={cc}&subject={subject}&body={body}"
    subprocess.run(['open', mailto_url])

def read_email(flag: bool, long: bool) -> str:
    ''' Flag:    True --> Accept | False --> Reject
        long: True --> Student has requested more than 4 days of extension time
    '''
    if long:
        with open('email_meeting.txt', 'r') as f:
            return f.read()
    if flag:
        with open('email_accept.txt', 'r') as f:
            return f.read()
    else:
        with open('email_reject.txt', 'r') as f:
            return f.read()

if __name__ == "__main__":
    print("GENERATING EMAIL STUFF...\n")
    main()



###

# Used for debug

###
def write_email(email_body: str, subject: str, to: str, cc: str):
    to_write = f"Subject: {subject}\nTo: {to}\nCC: {cc}\n\n{email_body}"
    with open('email.txt', 'w') as f:
        f.write(to_write)

def print_args():
    print("Arguments provided:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")